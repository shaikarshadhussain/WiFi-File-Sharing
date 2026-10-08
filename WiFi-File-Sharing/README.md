# Wi-Fi Based Local File Sharing System

**Project Title:** Wi-Fi Based Local File Sharing System  
**Subject:** Short Range Wireless Communication  
**Student Name:** [Your Name]  
**Register Number:** [Your Register Number]  
**Department:** Computer Science Engineering  
**Institution:** SRM University Ramapuram, Chennai  
**Academic Year:** 2026

## 1. Introduction

WiFi Share is a browser-based system for transferring files between devices connected to the same Wi-Fi or local area network (LAN). Files are stored only on the computer running the Flask server. It does not use cloud storage, email, or a third-party sharing service.

## 2. Problem Statement

Traditional sharing may require internet access, cloud accounts, USB drives, or messaging apps. This project provides a simple local alternative for short-range file transfer using a Wi-Fi router and HTTP.

## 3. Objectives

- Transfer files over local Wi-Fi.
- Avoid dependency on cloud services and internet connectivity.
- Provide a simple interface for multiple devices on the same network.
- Demonstrate Wi-Fi/LAN short-range wireless communication concepts.

## 4. Key Features

- Real upload, download, and delete operations
- Detected local network address and copy-link button
- Optional locally generated QR code for quick phone connection
- Drag-and-drop upload with progress indicator
- File statistics, search, and sorting
- Responsive light/dark dashboard
- 100 MB configurable upload limit and configurable allowed extensions
- Safe filenames, duplicate name handling, and path-traversal protection

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Flask | Local HTTP web server |
| HTML/CSS/JavaScript | Browser interface and interaction |
| Wi-Fi/LAN | Short-range network communication |
| QR Code | Easy mobile-device connection |

## 6. System Architecture

```text
Client Device (phone/laptop)
           ↓ HTTP over same Wi-Fi/LAN
        Flask Server
           ↓
      Local uploads/ folder
```

## 7. How It Works

1. Start `app.py` on the host laptop.
2. Flask detects a local IP address and listens on all interfaces using `0.0.0.0`.
3. A second device connects to the same Wi-Fi and opens `http://LOCAL_IP:5000`.
4. The device uploads a permitted file through HTTP; Flask stores it in `uploads/`.
5. Any connected device can list and download that file. Deleting removes it from the host folder.

## 8. Installation

```bash
git clone <repository-url>
cd WiFi-File-Sharing
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install and run:

```bash
pip install -r requirements.txt
python app.py
```

## 9. Access from Another Device

1. Connect the phone and host computer to the same Wi-Fi router.
2. Run `python app.py` on the computer.
3. Copy the displayed local URL, for example `http://192.168.1.105:5000`.
4. Open it on the phone or scan the QR code.
5. If Windows Firewall asks, allow Python on **Private networks**.

## 10. Internet Requirement

**Internet is not required.** The router only provides a local connection between devices; it does not need an internet connection. Both devices must be on the same Wi-Fi/LAN, and the host computer must remain running.

## 11. Demonstration Procedure

Start the server on Device 1 (laptop), open the local address on Device 2 (Android phone), upload `photo.pdf` from the phone, confirm it appears in the dashboard, then download it from either device. Finally use Delete and confirm the file disappears.

## 12. Security Considerations

- Werkzeug `secure_filename()` sanitizes uploaded names.
- Only configured common extensions are accepted.
- Maximum request size is 100 MB (change in `config.py`).
- Download/delete names must be direct children of `uploads/`; arbitrary paths are rejected.
- Duplicate names are safely changed to `name_1.ext`, `name_2.ext`.

This is an educational local-network project, not a production public file server. It has no authentication or encryption; do not expose it to the public internet.

## 13. Limitations

- Devices must use the same network.
- Wi-Fi speed affects transfer speed.
- The host must keep Flask running.
- No authentication, transfer resume, or public internet access is included.

## 14. Future Enhancements

Authentication, password-protected rooms, end-to-end encryption, previews, simultaneous transfers, resumable uploads, file expiry, WebSocket progress, Android app, Bluetooth support, and peer-to-peer transfer.

## 15. Advantages

Easy to use, fast on a local network, internet-free, cloud-free, cross-platform through a browser, and simple enough to explain in a viva.

## 16. Testing Checklist

| Test | Expected result |
|---|---|
| Open website locally | Dashboard loads successfully |
| Upload PDF | File appears in list |
| Download PDF | Browser downloads file |
| Delete PDF | File disappears from list |
| Open from phone on same Wi-Fi | Dashboard loads |
| Upload from phone | File appears on host |
| Oversized upload | Friendly size-limit error |
| Invalid extension | Friendly invalid-type error |
| Search | Only matching files appear |
| Sort | Files reorder by selected option |

## 17. Viva Questions and Answers

1. **What is Wi-Fi?** A wireless technology that connects devices over a local radio network.
2. **What is short-range wireless communication?** Data exchange over a limited local area, such as Wi-Fi or Bluetooth.
3. **Why use Wi-Fi?** It is common, fast, and lets many nearby devices connect.
4. **Does this application require internet?** No; it only needs a shared local network.
5. **What is a LAN?** A local area network connecting devices in a limited location.
6. **What is an IP address?** A numerical network address that identifies a device.
7. **Why is Flask used?** It is a lightweight Python framework for serving HTTP pages and APIs.
8. **What is HTTP?** The web protocol used by browser and server to exchange requests and responses.
9. **How does upload work?** The browser sends multipart file data to Flask, which validates and saves it.
10. **How does another device access the server?** It opens the host computer’s local IP and port 5000.
11. **What is `0.0.0.0`?** A bind address that makes Flask listen on available network interfaces.
12. **Why port 5000?** It is Flask’s commonly used development port.
13. **Which security measures are used?** Filename sanitization, extension checks, size limits, and path validation.
14. **What are the limitations?** Same network requirement, host availability, and no authentication.
15. **How can this project improve?** Add authentication, encryption, previews, and resumable uploads.
16. **Where are files stored?** In the host computer’s local `uploads/` directory.
17. **Why is this not cloud storage?** Files remain on the host machine and no external service is used.

## 18. Conclusion

This project demonstrates that a Flask server and local Wi-Fi/LAN can provide real browser-based file transfer without internet or cloud services. It is a clear practical example of short-range wireless communication.
