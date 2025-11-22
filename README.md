# Ceasor_Cipher
A program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

## GUI

A simple Tkinter GUI is provided in `gui.py`.

Run the GUI with Python (PowerShell):

```powershell
python gui.py
```

Shortcuts:
- Ctrl+E : Encrypt
- Ctrl+D : Decrypt

## Web server (browser)

You can also run a small web server that serves a browser UI. From the project root, create a virtual environment (recommended), install requirements, and run the server:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in a browser. The page has Encrypt / Decrypt / Brute-force (show all 26 possibilities) options.

## Instant browser UI (no Python required)

If you don't have Python installed (or prefer not to install it), there's a static browser page you can open directly without a server. Open the file:

```
web_static\index.html
```

Double-click the file or open it from your browser (File → Open File) and you can encrypt, decrypt, or run a brute-force attack entirely in the browser. This version uses the same Caesar logic ported to JavaScript and preserves case and punctuation.
