# WiFi Share

WiFi Share is a simple local file-sharing website. It lets phones, laptops, and tablets upload, download, and manage files when they are connected to the same Wi-Fi or local network.

Files stay on the computer running the Flask server. No internet connection, cloud account, email, or third-party sharing service is required.

## Features

- Upload, download, and delete real files
- Share files with devices connected to the same Wi-Fi/LAN
- Displays the local network address with a copy-link button
- Generates a QR code for easy phone access
- Drag-and-drop upload with progress feedback
- Search and sort available files
- Displays file name, type, size, and upload time
- Shows total file and storage statistics
- Responsive design for desktop and mobile
- Optional dark mode
- Safe file names and duplicate-file handling
- Configurable allowed file types and upload-size limit

## Built With

- Python
- Flask
- HTML, CSS, and vanilla JavaScript
- Local filesystem storage
- Wi-Fi / LAN using HTTP

## How It Works

```text
Phone or Laptop
       │
       │ HTTP over the same Wi-Fi / LAN
       ▼
Flask Server on Host Computer
       │
       ▼
Local uploads/ folder
```

Start the server on one computer. Open its local network address on another device connected to the same Wi-Fi. The connected device can then upload or download files through its browser.

## Installation

Clone the repository and open the project folder:

```bash
git clone <your-repository-url>
cd WiFi-File-Sharing
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python app.py
```

## Connect Another Device

1. Connect both devices to the same Wi-Fi network.
2. Run `python app.py` on the host computer.
3. Copy the local URL shown in the terminal or dashboard.
4. Open that URL on the other device, for example:

   ```text
   http://192.168.1.105:5000
   ```

5. Upload, download, and manage files from the browser.

You can also scan the QR code shown on the dashboard.

> If Windows Firewall asks for permission, allow Python on **Private networks**.

## Internet Requirement

Internet is **not required**. The devices only need to be connected to the same local Wi-Fi or LAN. The Wi-Fi router can work without an internet connection.

## Allowed File Types

The default supported extensions are:

```text
PDF, DOC, DOCX, TXT, PPT, PPTX, XLS, XLSX,
JPG, JPEG, PNG, GIF, MP3, MP4, ZIP, RAR, CSV
```

The file types and the default 100 MB upload limit can be changed in `config.py`.

## API Routes

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Opens the dashboard |
| `GET` | `/api/files` | Gets available files and statistics |
| `POST` | `/upload` | Uploads a file |
| `GET` | `/download/<filename>` | Downloads a file |
| `DELETE` | `/delete/<filename>` | Deletes a file |
| `GET` | `/network-info` | Gets the local network address |

## Security Notes

- Uploaded file names are sanitized.
- Only configured file extensions are accepted.
- Files larger than the configured limit are rejected.
- Duplicate file names are renamed safely.
- Download and delete operations are restricted to the `uploads/` folder.
- Path-traversal attempts are rejected.

This application is designed for trusted local networks. Do not expose the Flask development server to the public internet.

## Project Structure

```text
WiFi-File-Sharing/
├── app.py
├── config.py
├── requirements.txt
├── uploads/
├── templates/
└── static/
```
