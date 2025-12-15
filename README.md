# Pass-Strength-Analyzer-Breach-Detector

Project Cybersecurity

# Overview :

The **Pass Strength Analyzer Breach Detector** is a multi‑feature cybersecurity application built for educational and practical use.
It has the following featuers :

- Analyze password strength

- Check if a password appears in breach databases

- Generate strong, random passwords

- Hash & securely store passwords

- Use a friendly Tkinter-based GUI

# Project Features :

### Feature A — Password Strength Analyzer:

Uses regex-based rules and scoring to evaluate:

- Length quality

- Uppercase / lowercase usage

- Numbers

- Special characters

- Common weak patterns
  Final strength rating: > Weak / Medium / Strong

### Feature B — Breach Detector :

Checks password exposure using Local hashed breach list (rockyou-hashed.txt) , and HIBP API (k‑anonymity SHA1 range search)

**Outputs**: Not breached or Password found in breaches

### Feature C — Password Generator :

Generates randomized secure passwords with:> Uppercase , Lowercase , Numbers , Symbols

### Feature D — Secure Password Storage :

Hashes passwords using **SHA256** , Stores them safely in a file **(stored_passwords.txt)** revents storing plaintext passwords

# Tech Stack :

| Component        | Tech                       |
| ---------------- | -------------------------- |
| Language         | Python 3.11+               |
| GUI              | Tkinter                    |
| Password Hashing | hashlib                    |
| Breach Checking  | HIBP API + local hash list |
| Storage          | Text file storage          |

# How to Run the Project :

1. Install Python
2. Install dependencies -> `pip install requests`
3. Run the GUI -> `python UI.py`
