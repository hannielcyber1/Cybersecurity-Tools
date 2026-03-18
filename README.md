# 🔒 Cybersecurity Python Projects 🚀

This collection contains ** 5 projects** for educational and security testing purposes. Each project focuses on a specific area in cybersecurity — from Network scanning to password strength and brute-force testing.

---




## 1️⃣ Password Strength Checker
  
Evaluates password strength using length and complexity.

### 🚀 Features
- Checks:
  - Minimum 8 characters
  - Lowercase
  - Uppercase
  - Numbers
  - Special characters (@$!%*?&)
- Score out of 5 with suggestions.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python PASSWORD_CHECKER.py
```

### 🧪 Example
```
Enter password: Welcome123
Strength Score: 4/5
Suggestions: Add at least one special character.
```

---



## 2️⃣🔒🔑 Password List Generator 


A simple Python script that generates large **random password lists** and saves them to a file.
The generator creates passwords using a mixture of:

* lowercase letters
* uppercase letters
* numbers
* symbols and punctuation

This project is useful for **learning cybersecurity concepts**, **password testing**, and **creating custom wordlists for security research**.

---

### 🚀 Features

* 🔐 Generates **strong random passwords**
* 📏 User chooses **minimum and maximum password length**
* 🔢 User chooses **number of passwords to generate**
* 🔀 Uses **letters, numbers, and punctuation**
* 💾 Saves all passwords to a **`.lst` wordlist file**
* ⚡ Can generate **millions of passwords**

---

### 📂 Project Structure

```
📁 Password-List-Generator
│
├── Password_List_Generator.py   # Password list generator script
└── README.md               # Project documentation
```

---

### ⚙️ Requirements

* Python **3.x**
* No external libraries required

The script uses only built-in Python modules:

* `random`
* `string`

---

### ▶️ Usage

Run the script:

```
python Password_List_Generator.py
```

You will be asked for the password settings:

```
Enter minimum password length: 8
Enter maximum password length: 16
Enter number of passwords to generate: 1000000
```

---

### 📄 Output

The generated passwords are saved in a file called:

```
password.lst
```

Example content:

```
aF#8kL!2
P@9xZ!q$2
mD#7^q1B@x
t$G8@z!P2L
```

---

## 3️⃣🔐 Encryption & Decryption Toolkit

This project provides simple command-line tools for **text encryption and decryption** using three classic cipher techniques:  

- **Caesar Cipher**  
- **XOR Cipher**  
- **Vigenère Cipher**  

The toolkit is split into two scripts:  

- `ENCRYPTION_TOOL.py` → Encrypts plaintext into ciphertext.  
- `DECRYPTION_TOOL.py` → Decrypts ciphertext back into plaintext.  

---

### 🚀 Features

- Interactive command-line interface.  
- Supports **three different cipher algorithms**.  
- Input validation (keys must match expected format).  
- Works with uppercase and lowercase letters.  
- Lightweight — no external dependencies required.  

---

### 📂 Project Structure

```
📁 Encryption-Decryption-Toolkit
 ├── ENCRYPTION_TOOL.py   # Encrypts text
 ├── DECRYPTION_TOOL.py   # Decrypts text
 └── README.md            # Project documentation
```

---

### ⚙️ Installation

1. Clone or download the project folder.  
2. Ensure you have **Python 3.x** installed on your system.  
3. Run the scripts directly with Python:

```bash
python ENCRYPTION_TOOL.py
python DECRYPTION_TOOL.py
```

---

### 🛠️ Usage

### 1. Encryption
Run the encryption tool:

```bash
python ENCRYPTION_TOOL.py
```

Steps:
1. Choose a cipher method:  
   - `1` → Caesar Cipher  
   - `2` → XOR Cipher  
   - `3` → Vigenère Cipher  
2. Enter the text you want to encrypt.  
3. Provide the encryption key depending on the cipher.  
4. The encrypted text is displayed.  

---

### 2. Decryption
Run the decryption tool:

```bash
python DECRYPTION_TOOL.py
```

Steps:
1. Choose the cipher method used during encryption.  
2. Enter the encrypted text.  
3. Provide the decryption key (must match the encryption key).  
4. The decrypted text is displayed.  

---

### 🔑 Cipher Details

### Caesar Cipher
- Shifts each letter by a numeric key.  
- Example: `"HELLO"` with key `3` → `"KHOOR"`.  

### XOR Cipher
- Applies bitwise XOR with a numeric key (`1–255`).  
- Symmetric: encryption and decryption use the same operation.  

### Vigenère Cipher
- Uses a keyword of letters to determine shifting for each character.  
- Example: Text `"HELLO"`, Key `"KEY"` → `"RIJVS"`.  

---

### 📌 Example Workflow

**Encryption (Caesar Cipher):**
```
=== ENCRYPTION TOOL ===
Choose a cipher method:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the text to encrypt: HELLO
Enter the shift key (number): 3

Original text: HELLO
Caesar key: 3
Encrypted text: KHOOR
```

**Decryption (Caesar Cipher):**
```
=== DECRYPTION TOOL ===
Choose the cipher method used for encryption:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the encrypted text: KHOOR
Enter the shift key used for encryption: 3

Encrypted text: KHOOR
Caesar key: 3
Decrypted text: HELLO
```

---

## 4️⃣🔎 Python Port Scanner

A lightweight **Python port scanner** that checks common ports on a target host and reports whether they are **open or closed**.

This project demonstrates **basic network scanning using Python sockets** and is ideal for beginners learning **cybersecurity, networking, and penetration testing fundamentals**.

---

### 📜 Script

The project contains one main script:

* `Simple_Portscanner.py` → Scans selected ports on a target host and displays their status.

---

### 🚀 Features

* Simple command-line port scanner
* Detects **open and closed ports**
* Displays the **service associated with each port**
* Uses Python’s built-in **socket module**
* Fast scanning using connection timeouts
* Lightweight — **no external dependencies required**

---

### 🌐 Ports Scanned

The scanner checks several common ports used by popular services.

| Port | Service |
| ---- | ------- |
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 80   | HTTP    |
| 443  | HTTPS   |
| 445  | SMB     |
| 3389 | RDP     |

---

### 📂 Project Structure

```
📁 Python-Port-Scanner
│
├── Simple_Portscanner.py   # Main port scanner
└── README.md         # Project documentation
```

---

### ⚙️ Requirements
* Python **3.x**
* No external libraries required

---

### ▶️ Usage

Run the script:

```
python Simple_Portscanner.py
```

Example output:

```
21 IS CLOSED. SERVICE: FTP
22 IS OPEN. SERVICE: SSH
23 IS CLOSED. SERVICE: Telnet
80 IS OPEN. SERVICE: HTTP
443 IS OPEN. SERVICE: HTTPS
445 IS CLOSED. SERVICE: SMB
3389 IS CLOSED. SERVICE: RDP
```

---


## 5️⃣🔎 Multithreaded Python Port Scanner

A fast **multithreaded port scanner written in Python** that scans **ports 1–65535** on any target host.
The scanner displays **colored results in the terminal** and **saves open ports to a file** for later analysis.

This project is designed for learning **network security, socket programming, and penetration testing fundamentals**.

---

### 🚀 Features

* 🌍 Scan **any IP address or hostname**
* ⚡ **Multithreaded scanning** for faster results
* 🔎 Scan **ports 1–65535**
* 🎨 **Colored terminal output**
* 💾 **Automatically saves results to a file**
* 🧠 Built using **Python socket programming**
* 📦 Uses only **built-in Python libraries**

---

### 📂 Project Structure

```
📁 Python-Port-Scanner
│
├── MULTITHREAD_PORT_SCANNER.py     # Multithreaded port scanner
└── README.md           # Project documentation
```

---

### ⚙️ Requirements

* Python **3.x**
* No external libraries required

The scanner only uses built-in Python modules:

* `socket`
* `threading`
* `queue`
* `datetime`

---

### ▶️ Usage

Run the scanner:

```
python MULTITHREAD_PORT_SCANNER.py
```

Enter the target when prompted:

```
Enter target IP or hostname: scanme.nmap.org
```

---

### 📊 Example Output

```
===================================
  MULTITHREADED PYTHON PORT SCANNER
===================================

Scanning target: 45.33.32.156
Ports: 1 - 65535

[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 9929

Scan completed at: 2026-03-16 23:20:12
Results saved to: scan_results_45.33.32.156.txt
```

---

### 💾 Saved Results

After the scan completes, results are automatically saved to a file:

```
scan_results_<target-ip>.txt
```

Example:

```
scan_results_45.33.32.156.txt
```

File content example:

```
Port Scan Results for 45.33.32.156

Port 22 OPEN
Port 80 OPEN
Port 9929 OPEN
```

---


