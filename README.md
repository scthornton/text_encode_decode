# 🔐 Text Encoder/Decoder

<div align="center">

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)

A comprehensive Python tool for encoding and decoding text using various encoding schemes.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Encodings](#supported-encodings) • [Examples](#examples) • [API](#api-documentation)

</div>

---

## ✨ Features

- 🚀 **Multiple Encoding Schemes** - Support for Base64, Base32, Hex, URL, HTML, ROT13, and ASCII85
- 📝 **Simple CLI Interface** - Easy-to-use command-line interface
- 🔄 **Bidirectional** - Encode and decode with the same tool
- 📚 **Well-Documented** - Comprehensive documentation with analogies and examples
- 🐍 **Pure Python** - No external dependencies required
- 📊 **Pipe Support** - Works seamlessly with Unix pipes

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher

### Quick Start

1. Clone this repository:
```bash
git clone https://github.com/scthornton/text_encode_decode.git
cd text_encode_decode
```

2. Make the script executable (optional):
```bash
chmod +x text_codec.py
```

3. Run the tool:
```bash
python text_codec.py --help
```

## 📖 Usage

### Basic Commands

#### Encoding Text
```bash
python text_codec.py -e base64 "Hello, World!"
# Output: SGVsbG8sIFdvcmxkIQ==
```

#### Decoding Text
```bash
python text_codec.py -d base64 "SGVsbG8sIFdvcmxkIQ=="
# Output: Hello, World!
```

#### List Available Encodings
```bash
python text_codec.py --list
```

### Using with Pipes

```bash
echo "Secret Message" | python text_codec.py -e hex
# Output: 536563726574204d657373616765

cat file.txt | python text_codec.py -e base64 > encoded.txt
```

## 🔤 Supported Encodings

| Encoding | Description | Use Cases |
|----------|-------------|-----------|
| **base64** | Base64 encoding (RFC 4648) | Email attachments, Data URLs, API tokens |
| **base32** | Base32 encoding (RFC 4648) | Case-insensitive systems, File sharing |
| **hex** | Hexadecimal encoding | Color codes, Memory addresses, Debugging |
| **url** | URL/Percent encoding (RFC 3986) | Web URLs, Query parameters |
| **html** | HTML entity encoding | Web content, Preventing XSS |
| **rot13** | ROT13 substitution cipher | Simple obfuscation, Spoiler text |
| **ascii85** | ASCII85/Base85 encoding | PDF files, More efficient than Base64 |
| **binary** | Binary representation (base 2) | Low-level debugging, Education, Bit manipulation |
| **octal** | Octal representation (base 8) | Unix permissions, Legacy systems, Escape sequences |

## 💡 Examples

### Base64 Encoding/Decoding
```bash
# Encode a password
python text_codec.py -e base64 "MySecretPassword123!"
# Output: TXlTZWNyZXRQYXNzd29yZDEyMyE=

# Decode
python text_codec.py -d base64 "TXlTZWNyZXRQYXNzd29yZDEyMyE="
# Output: MySecretPassword123!
```

### URL Encoding for Web
```bash
# Encode a URL parameter
python text_codec.py -e url "Hello World & Friends!"
# Output: Hello%20World%20%26%20Friends%21
```

### HTML Encoding for Safety
```bash
# Encode HTML to prevent XSS
python text_codec.py -e html '<script>alert("XSS")</script>'
# Output: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;
```

### Hexadecimal for Debugging
```bash
# Convert text to hex for analysis
python text_codec.py -e hex "🔐🚀"
# Output: f09f9490f09f9a80
```

### Binary Representation
```bash
# See the binary representation of text
python text_codec.py -e binary "Hi!"
# Output: 01001000 01101001 00100001

# Decode binary back to text
python text_codec.py -d binary "01001000 01101001 00100001"
# Output: Hi!
```

### Octal Encoding
```bash
# Convert to octal (base 8)
python text_codec.py -e octal "ABC"
# Output: 101 102 103

# Useful for Unix permissions representation
python text_codec.py -e octal "rwx"
# Output: 162 167 170
```

### Chain Operations
```bash
# Encode with base64, then encode the result with URL encoding
echo "Special/Characters+Here" | python text_codec.py -e base64 | python text_codec.py -e url
```

## 📚 API Documentation

### Using as a Python Module

```python
from text_codec import EncoderDecoder

# Create an instance
encoder = EncoderDecoder()

# Encode text
encoded = encoder.encode("Hello, World!", "base64")
print(encoded)  # SGVsbG8sIFdvcmxkIQ==

# Decode text
decoded = encoder.decode("SGVsbG8sIFdvcmxkIQ==", "base64")
print(decoded)  # Hello, World!

# List available encodings
encodings = encoder.list_encodings()
for name, description in encodings.items():
    print(f"{name}: {description}")
```

### Direct Access to Encoding Functions

```python
from text_codec import TextEncoder

# Use individual encoding methods
text = "Hello, World!"
base64_encoded = TextEncoder.base64_encode(text)
hex_encoded = TextEncoder.hex_encode(text)
url_encoded = TextEncoder.url_encode(text)
```

## 🧠 Understanding Encodings (With Analogies)

### Base64
Think of Base64 like converting a book into a series of QR codes - it takes any data and represents it using only 64 different characters. It's like having a universal alphabet that computers everywhere can understand.

### Hexadecimal
Hex encoding is like describing colors to someone using only numbers - each byte of data is represented as two hexadecimal digits (0-9, A-F). It's the "native language" of computer memory.

### URL Encoding
URL encoding is like preparing text for a journey through the internet - spaces become `%20`, special characters get "travel visas" in the form of `%XX` codes. It ensures your text arrives safely at its destination.

### HTML Encoding
HTML encoding is like putting text in protective bubble wrap before displaying it on a webpage - dangerous characters like `<` and `>` are converted to safe representations like `&lt;` and `&gt;`.

### Binary
Binary encoding is like seeing the world through a computer's eyes - everything is reduced to 1s and 0s, like a series of on/off switches. Each character becomes 8 bits (one byte), making it perfect for understanding how data is stored at the lowest level.

### Octal
Octal is like binary's more compact cousin - instead of using just 0 and 1, it uses digits 0-7. Imagine if you were counting on your hands but only had 8 fingers total. It's particularly famous in Unix/Linux for file permissions (like chmod 755).

## 🔒 Security Considerations

- **Encoding ≠ Encryption**: These encodings are NOT secure. They're transformations, not encryption.
- **ROT13**: This is a simple letter substitution - it's for obfuscation, not security.
- **Use Cases**: Use these encodings for data transmission, storage, and display - not for securing sensitive information.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the need for a simple, unified encoding/decoding tool
- Built with Python's excellent standard library
- Special thanks to the Python community

---

<div align="center">
Made with ❤️ and 🐍 Python
</div>
