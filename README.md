# codeorbitproject2ceasercipher
A Python-based Caesar Cipher Encryption Tool that allows users to encrypt and decrypt messages using a customizable shift key. It supports uppercase and lowercase letters while preserving spaces, numbers, and special characters. Includes an interactive menu for encryption,decryption,demonstration,with input validation for a better user experience.
# 🔐 Caesar Cipher Encryption Tool (Python)

## 📌 Project Overview

The **Caesar Cipher Encryption Tool** is a simple Python-based cryptography project that allows users to encrypt and decrypt messages using the Caesar Cipher technique.

It works by shifting each letter in a message by a fixed number of positions in the alphabet using a user-defined key. The program provides an interactive menu for encryption, decryption, and testing both operations.

## ✨ Features

- **Message Encryption:** Converts plain text into encrypted text.
- **Message Decryption:** Converts encrypted text back into the original message.
- **Custom Shift Key:** Allows users to enter their own integer key.
- **Uppercase & Lowercase Support:** Handles both capital and small letters.
- **Special Character Support:** Preserves spaces, numbers, and punctuation.
- **Input Validation:** Handles invalid key inputs.
- **Interactive Menu:** Simple menu-driven interface.
- **Demo Mode:** Encrypts and decrypts a message in one operation.

## 🛠️ Technologies Used

- Python 3
- Built-in Python Functions
- Basic Cryptography
- Conditional Statements
- Loops and Functions
- ASCII Values (`ord()` and `chr()`)

## ⚙️ How It Works

The Caesar Cipher is a substitution encryption technique in which each letter is shifted by a fixed number of positions in the alphabet.

**Example (Shift Key = 2):**

| Original Text | Encrypted Text |
|---|---|
| HELLO | JGNNQ |
| KARTHIK | MCTVJMK |

- **Encryption:** Shifts letters forward based on the key.
- **Decryption:** Shifts letters backward using the same key.
- **Modulo (26):** Ensures letters wrap around the alphabet.

## 📂 Project Structure

```text
Caesar-Cipher/
│
├── ceasecipher.py
└── README.md
```

## 🚀 How to Run the Project

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd Caesar-Cipher
```

**Step 3: Run the Python program**

```bash
python ceasecipher.py
```

**Note:** Python 3 must be installed on your system.

## 💻 Program Options

When you run the program, you will see four options:

1. Encrypt a message
2. Decrypt a message
3. Encrypt and then decrypt (Demo)
4. Exit

Select an option and enter your message and shift key.

## 📸 Sample Output

```text
=============================================
        CAESAR CIPHER ENCRYPTION TOOL
=============================================

1. Encrypt a message
2. Decrypt a message
3. Encrypt and then decrypt (demo)
4. Exit

Choose an option (1-4): 1
Enter plain text: karthik
Enter shift value (key): 2

--- Result ---
Original text  : karthik
Shift (key)    : 2
Encrypted text : mctvjkm
```

**Decryption Example:**

```text
Choose an option (1-4): 2
Enter cipher text: mctvjkm
Enter shift value (key): 2

--- Result ---
Cipher text    : mctvjkm
Shift (key)    : 2
Decrypted text : karthik
```

## 🎯 Learning Outcomes

Through this project, I learned:

- Fundamentals of cryptography.
- Implementation of Caesar Cipher encryption and decryption.
- String manipulation in Python.
- Using ASCII values to shift characters.
- Implementing loops, functions, and conditional statements.
- Handling invalid user inputs.

## ⚠️ Security Note

The Caesar Cipher is a basic educational encryption technique. It is not suitable for protecting sensitive information because it can be easily broken.

## 👨‍💻 Author

**Karthik Reddy**

## ⭐ Conclusion

This project demonstrates the basic working principle of the Caesar Cipher using Python. It provides a simple, interactive way to understand encryption, decryption, and fundamental cryptography concepts.

If you find this project useful, consider giving the repository a ⭐ star!



