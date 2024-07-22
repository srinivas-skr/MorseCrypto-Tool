# MorseCrypto-Tool

# MorseCrypto Tool

**MorseCrypto Tool** is a Python-based application that combines Morse code conversion with AES encryption and decryption functionalities. This tool is designed to provide users with a practical means of secure text handling and encoding.

## Features

- **Morse Code Conversion**:
  - Convert text to Morse code.
  - Convert Morse code back to text.

- **AES Encryption/Decryption**:
  - Encrypt and decrypt text using AES (Advanced Encryption Standard).
  - Base64 encoding is used for displaying encrypted messages.


## Example

### Morse Code Conversion

- **Text to Morse Code**:
    ```
    Enter text to convert to Morse code: HELLO
    Morse Code: .... . .-.. .-.. ---
    ```

- **Morse Code to Text**:
    ```
    Enter Morse code to convert to text: .... . .-.. .-.. ---
    Text: HELLO
    ```

### AES Encryption/Decryption

- **Encrypt**:
    ```
    Enter message to encrypt: SECRET
    Encrypted message (base64): <base64-encoded-string>
    ```

- **Decrypt**:
    ```
    Enter encrypted message to decrypt: <base64-encoded-string>
    Decrypted message: SECRET
    ```
