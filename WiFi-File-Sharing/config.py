from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100 MB
ALLOWED_EXTENSIONS = {
    "pdf", "doc", "docx", "txt", "ppt", "pptx", "xls", "xlsx",
    "jpg", "jpeg", "png", "gif", "mp3", "mp4", "zip", "rar", "csv",
}
