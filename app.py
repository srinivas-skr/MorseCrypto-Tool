from flask import Flask, request, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

app = Flask(__name__)

# AES Encryption technique
key = b'Sixteen byte key'  # 16 bytes key for AES

def aes_encrypt(text):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def aes_decrypt(iv, ct):
    iv = b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Morse Code Conversion
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '"': '.-..-.', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(i.upper(), '') for i in text)

def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(i, '') for i in morse.split(' '))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text')
    iv, ct = aes_encrypt(text)
    return render_template('index.html', iv=iv, ciphertext=ct)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    iv = request.form.get('iv')
    ct = request.form.get('ciphertext')
    plaintext = aes_decrypt(iv, ct)
    return render_template('index.html', plaintext=plaintext)

@app.route('/morse', methods=['POST'])
def morse_conversion():
    text = request.form.get('text')
    morse_code = text_to_morse(text)
    return render_template('index.html', morse=morse_code)

@app.route('/from_morse', methods=['POST'])
def from_morse_conversion():
    morse_code = request.form.get('morse')
    text = morse_to_text(morse_code)
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
