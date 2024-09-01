
---

# Caesar Cipher Encryption and Decryption

This project provides a simple implementation of the Caesar Cipher, a basic encryption technique where each letter in a message is shifted by a certain number of positions in the alphabet. This script allows you to encrypt and decrypt messages using the Caesar Cipher technique.

## Introduction

The Caesar Cipher is one of the oldest and simplest methods of encryption. It involves shifting the letters in a message by a fixed number of positions in the alphabet. This Python script provides a basic implementation for both encryption and decryption of messages using the Caesar Cipher technique.

## Features

- **Encryption:** Encrypts a message by shifting its characters by a specified number of positions in the alphabet.
- **Decryption:** Decrypts an encrypted message by reversing the shift.
- **Supports Uppercase and Lowercase Letters:** Handles both uppercase and lowercase letters, maintaining the case.
- **Handles Non-Alphabetic Characters:** Leaves non-alphabetic characters (e.g., numbers, punctuation) unchanged.

## Prerequisites

To run this script, you'll need:

- Python 3.x installed on your machine.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Prodigy-infoTech_cs_intern_01
   ```

3. No additional libraries are required as this script uses only Python's standard libraries.

## Usage

1. Run the script using Python:

   ```bash
   python caesar_cipher.py
   ```

2. The script will prompt you to enter the message you want to encrypt and the shift value:

   - **Enter your message**: Provide the message you want to encrypt.
   - **Enter the shift value**: Specify the number of positions by which you want to shift the letters.

3. The script will then display the encrypted message and decrypt it back to the original message.

### Example:

```bash
Enter your message: Hello, World!
Enter the shift value: 3
Encrypted Message: Khoor, Zruog!
Decrypted Message: Hello, World!
```

In this example, each letter in the message "Hello, World!" is shifted by 3 positions in the alphabet. The script then decrypts the encrypted message back to the original text.

## Functions Overview

- **caesar_cipher(message, shift, mode='encrypt'):**
  - **Description:** Encrypts or decrypts a message using the Caesar Cipher technique.
  - **Arguments:**
    - `message`: The message to be encrypted or decrypted.
    - `shift`: The number of positions to shift the characters.
    - `mode`: The mode of operation. Set to `'encrypt'` for encryption or `'decrypt'` for decryption.
  - **Returns:** The encrypted or decrypted message.

## File Structure

```bash
.
├── caesar_cipher.py       # Main script for Caesar Cipher encryption and decryption
└── README.md              # This README file
```

---

### Notes:
- Replace `"https://github.com/your-username/caesar-cipher.git"` with your actual GitHub repository URL.
- If you decide to include any test cases or additional features, update the README accordingly.
