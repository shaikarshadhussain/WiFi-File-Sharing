"""Wi-Fi Based Local File Sharing System - simple Flask backend."""
import socket
import base64
from io import BytesIO
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename

from config import ALLOWED_EXTENSIONS, MAX_UPLOAD_SIZE, UPLOAD_FOLDER

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_SIZE
UPLOAD_FOLDER.mkdir(exist_ok=True)


def get_local_ip():
    """Return the LAN address used by this computer, with a safe fallback."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.connect(("8.8.8.8", 80))
            return connection.getsockname()[0]
    except OSError:
        return "127.0.0.1"


def make_qr_code(url):
    """Make a local QR image. A missing optional QR package never stops the app."""
    try:
        import qrcode
        image = qrcode.make(url)
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")
    except Exception:
        return None


def human_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def unique_filename(filename):
    """Return a non-conflicting filename inside uploads."""
    path = Path(filename)
    candidate, counter = filename, 1
    while (UPLOAD_FOLDER / candidate).exists():
        candidate = f"{path.stem}_{counter}{path.suffix}"
        counter += 1
    return candidate


def file_icon(filename):
    extension = Path(filename).suffix.lower().lstrip(".")
    groups = {
        "pdf": "📄", "doc": "📝", "docx": "📝", "txt": "📃",
        "jpg": "🖼️", "jpeg": "🖼️", "png": "🖼️", "gif": "🖼️",
        "mp4": "🎬", "mp3": "🎵", "zip": "📦", "rar": "📦",
        "ppt": "📊", "pptx": "📊", "xls": "📈", "xlsx": "📈", "csv": "📈",
    }
    return groups.get(extension, "📁")


def list_files():
    files = []
    for file_path in UPLOAD_FOLDER.iterdir():
        if not file_path.is_file() or file_path.name == ".gitkeep":
            continue
        info = file_path.stat()
        files.append({
            "name": file_path.name,
            "size": info.st_size,
            "size_display": human_size(info.st_size),
            "uploaded_at": datetime.fromtimestamp(info.st_mtime).strftime("%d %b %Y, %I:%M %p"),
            "timestamp": info.st_mtime,
            "icon": file_icon(file_path.name),
        })
    return sorted(files, key=lambda item: item["timestamp"], reverse=True)


@app.get("/")
def index():
    ip = get_local_ip()
    url = f"http://{ip}:5000"
    return render_template("index.html", local_ip=ip, local_url=url, qr_code=make_qr_code(url), max_upload_mb=MAX_UPLOAD_SIZE // (1024 * 1024))


@app.get("/api/files")
def files_api():
    files = list_files()
    return jsonify({
        "files": files,
        "stats": {"total_files": len(files), "total_size": human_size(sum(item["size"] for item in files))},
    })


@app.get("/network-info")
def network_info():
    ip = get_local_ip()
    return jsonify({"ip": ip, "url": f"http://{ip}:5000"})


@app.post("/upload")
def upload():
    file = request.files.get("file")
    if not file or not file.filename:
        return jsonify(error="Please select a file."), 400
    cleaned_name = secure_filename(file.filename)
    if not cleaned_name:
        return jsonify(error="Please choose a valid filename."), 400
    if not allowed_file(cleaned_name):
        return jsonify(error="This file type is not allowed."), 400
    saved_name = unique_filename(cleaned_name)
    file.save(UPLOAD_FOLDER / saved_name)
    return jsonify(message="Upload successful.", filename=saved_name), 201


@app.get("/download/<path:filename>")
def download(filename):
    # Filename must resolve to a direct child of uploads, never an arbitrary path.
    if filename != secure_filename(filename) or not (UPLOAD_FOLDER / filename).is_file():
        return render_template("error.html", message="The requested file could not be found."), 404
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


@app.delete("/delete/<path:filename>")
def delete(filename):
    if filename != secure_filename(filename):
        return jsonify(error="Invalid filename."), 400
    target = UPLOAD_FOLDER / filename
    if not target.is_file():
        return jsonify(error="The requested file could not be found."), 404
    try:
        target.unlink()
        return jsonify(message="File deleted successfully.")
    except OSError:
        return jsonify(error="Unable to delete the file."), 500


@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(_error):
    return jsonify(error=f"File is too large. Maximum allowed size: {MAX_UPLOAD_SIZE // (1024 * 1024)} MB."), 413


@app.errorhandler(404)
def not_found(_error):
    return render_template("error.html", message="The page you requested could not be found."), 404


if __name__ == "__main__":
    print(f"WiFi Share is ready at http://{get_local_ip()}:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
