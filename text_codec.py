#!/usr/bin/env python3
"""
text_codec.py - Text Encoder/Decoder
A comprehensive tool for encoding and decoding text using various encoding schemes.
"""

import base64
import binascii
import urllib.parse
import html
import codecs
import argparse
import sys
from typing import Union, Dict, Callable


class TextEncoder:
    """
    A class that provides encoding and decoding functionality for various text encoding schemes.
    
    Think of this class like a universal translator for different text formats - similar to how
    a Swiss Army knife has different tools for different tasks, this class has different methods
    for different encoding schemes.
    """
    
    @staticmethod
    def base64_encode(text: str) -> str:
        """
        Encode text to Base64.
        
        Base64 is like converting text into a secret code using only 64 characters (A-Z, a-z, 0-9, +, /).
        It's commonly used in email attachments and data URLs.
        
        Args:
            text: The string to encode
            
        Returns:
            Base64 encoded string
        """
        return base64.b64encode(text.encode('utf-8')).decode('ascii')
    
    @staticmethod
    def base64_decode(encoded: str) -> str:
        """
        Decode Base64 text.
        
        Args:
            encoded: Base64 encoded string
            
        Returns:
            Decoded string
        """
        return base64.b64decode(encoded).decode('utf-8')
    
    @staticmethod
    def base32_encode(text: str) -> str:
        """
        Encode text to Base32.
        
        Base32 is like Base64's cousin - it uses only 32 characters (A-Z and 2-7).
        It's case-insensitive and often used in file sharing and authentication tokens.
        
        Args:
            text: The string to encode
            
        Returns:
            Base32 encoded string
        """
        return base64.b32encode(text.encode('utf-8')).decode('ascii')
    
    @staticmethod
    def base32_decode(encoded: str) -> str:
        """
        Decode Base32 text.
        
        Args:
            encoded: Base32 encoded string
            
        Returns:
            Decoded string
        """
        return base64.b32decode(encoded).decode('utf-8')
    
    @staticmethod
    def hex_encode(text: str) -> str:
        """
        Encode text to hexadecimal.
        
        Hex encoding is like representing each character as its numerical value in base 16.
        It's commonly used in color codes, memory addresses, and cryptographic hashes.
        
        Args:
            text: The string to encode
            
        Returns:
            Hexadecimal string
        """
        return text.encode('utf-8').hex()
    
    @staticmethod
    def hex_decode(encoded: str) -> str:
        """
        Decode hexadecimal text.
        
        Args:
            encoded: Hexadecimal string
            
        Returns:
            Decoded string
        """
        return bytes.fromhex(encoded).decode('utf-8')
    
    @staticmethod
    def url_encode(text: str) -> str:
        """
        URL encode text.
        
        URL encoding is like making text safe for web addresses - spaces become %20,
        special characters get converted to %XX format. Essential for web development.
        
        Args:
            text: The string to encode
            
        Returns:
            URL encoded string
        """
        return urllib.parse.quote(text)
    
    @staticmethod
    def url_decode(encoded: str) -> str:
        """
        Decode URL encoded text.
        
        Args:
            encoded: URL encoded string
            
        Returns:
            Decoded string
        """
        return urllib.parse.unquote(encoded)
    
    @staticmethod
    def html_encode(text: str) -> str:
        """
        HTML encode text.
        
        HTML encoding is like making text safe for web pages - < becomes &lt;,
        > becomes &gt;, etc. This prevents code injection and display issues.
        
        Args:
            text: The string to encode
            
        Returns:
            HTML encoded string
        """
        return html.escape(text)
    
    @staticmethod
    def html_decode(encoded: str) -> str:
        """
        Decode HTML encoded text.
        
        Args:
            encoded: HTML encoded string
            
        Returns:
            Decoded string
        """
        return html.unescape(encoded)
    
    @staticmethod
    def rot13_encode(text: str) -> str:
        """
        Encode text using ROT13.
        
        ROT13 is like a simple letter substitution cipher - each letter is replaced
        by the letter 13 positions after it in the alphabet. It's its own inverse!
        
        Args:
            text: The string to encode
            
        Returns:
            ROT13 encoded string
        """
        return codecs.encode(text, 'rot_13')
    
    @staticmethod
    def rot13_decode(encoded: str) -> str:
        """
        Decode ROT13 text.
        
        Args:
            encoded: ROT13 encoded string
            
        Returns:
            Decoded string
        """
        return codecs.decode(encoded, 'rot_13')
    
    @staticmethod
    def ascii85_encode(text: str) -> str:
        """
        Encode text to ASCII85 (Base85).
        
        ASCII85 is like a more efficient cousin of Base64 - it uses 85 printable
        ASCII characters and produces smaller output. Often used in PDF files.
        
        Args:
            text: The string to encode
            
        Returns:
            ASCII85 encoded string
        """
        return base64.a85encode(text.encode('utf-8')).decode('ascii')
    
    @staticmethod
    def ascii85_decode(encoded: str) -> str:
        """
        Decode ASCII85 text.
        
        Args:
            encoded: ASCII85 encoded string
            
        Returns:
            Decoded string
        """
        return base64.a85decode(encoded).decode('utf-8')
    
    @staticmethod
    def binary_encode(text: str) -> str:
        """
        Encode text to binary representation.
        
        Binary encoding is like translating text into the language of switches - 
        each character becomes a series of 1s and 0s (on/off). It's the most 
        fundamental way computers represent data internally.
        
        Args:
            text: The string to encode
            
        Returns:
            Binary string (space-separated bytes)
        """
        return ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))
    
    @staticmethod
    def binary_decode(encoded: str) -> str:
        """
        Decode binary text.
        
        Args:
            encoded: Binary string (space-separated bytes)
            
        Returns:
            Decoded string
        """
        # Remove any extra whitespace and split by spaces
        binary_bytes = encoded.strip().split()
        # Convert each binary string to a byte
        byte_array = bytearray(int(b, 2) for b in binary_bytes)
        return byte_array.decode('utf-8')
    
    @staticmethod
    def octal_encode(text: str) -> str:
        """
        Encode text to octal representation.
        
        Octal encoding is like binary's older sibling - instead of using just 0 and 1,
        it uses digits 0-7. It's like counting on your fingers if you only had 8 fingers.
        Historically used in Unix file permissions (e.g., chmod 755).
        
        Args:
            text: The string to encode
            
        Returns:
            Octal string (space-separated bytes)
        """
        return ' '.join(format(byte, '03o') for byte in text.encode('utf-8'))
    
    @staticmethod
    def octal_decode(encoded: str) -> str:
        """
        Decode octal text.
        
        Args:
            encoded: Octal string (space-separated bytes)
            
        Returns:
            Decoded string
        """
        # Remove any extra whitespace and split by spaces
        octal_bytes = encoded.strip().split()
        # Convert each octal string to a byte
        byte_array = bytearray(int(o, 8) for o in octal_bytes)
        return byte_array.decode('utf-8')


class EncoderDecoder:
    """
    Main class that orchestrates encoding and decoding operations.
    
    This is like the conductor of an orchestra - it coordinates all the different
    encoding methods and provides a unified interface to use them.
    """
    
    def __init__(self):
        self.encoder = TextEncoder()
        self.encodings: Dict[str, Dict[str, Callable]] = {
            'base64': {
                'encode': self.encoder.base64_encode,
                'decode': self.encoder.base64_decode,
                'description': 'Base64 encoding (RFC 4648)'
            },
            'base32': {
                'encode': self.encoder.base32_encode,
                'decode': self.encoder.base32_decode,
                'description': 'Base32 encoding (RFC 4648)'
            },
            'hex': {
                'encode': self.encoder.hex_encode,
                'decode': self.encoder.hex_decode,
                'description': 'Hexadecimal encoding'
            },
            'url': {
                'encode': self.encoder.url_encode,
                'decode': self.encoder.url_decode,
                'description': 'URL/Percent encoding (RFC 3986)'
            },
            'html': {
                'encode': self.encoder.html_encode,
                'decode': self.encoder.html_decode,
                'description': 'HTML entity encoding'
            },
            'rot13': {
                'encode': self.encoder.rot13_encode,
                'decode': self.encoder.rot13_decode,
                'description': 'ROT13 substitution cipher'
            },
            'ascii85': {
                'encode': self.encoder.ascii85_encode,
                'decode': self.encoder.ascii85_decode,
                'description': 'ASCII85/Base85 encoding'
            },
            'binary': {
                'encode': self.encoder.binary_encode,
                'decode': self.encoder.binary_decode,
                'description': 'Binary representation (base 2)'
            },
            'octal': {
                'encode': self.encoder.octal_encode,
                'decode': self.encoder.octal_decode,
                'description': 'Octal representation (base 8)'
            }
        }
    
    def encode(self, text: str, encoding: str) -> str:
        """
        Encode text using the specified encoding.
        
        Args:
            text: Text to encode
            encoding: Encoding type (base64, hex, url, etc.)
            
        Returns:
            Encoded string
            
        Raises:
            ValueError: If encoding type is not supported
        """
        if encoding not in self.encodings:
            raise ValueError(f"Unsupported encoding: {encoding}")
        return self.encodings[encoding]['encode'](text)
    
    def decode(self, text: str, encoding: str) -> str:
        """
        Decode text using the specified encoding.
        
        Args:
            text: Text to decode
            encoding: Encoding type (base64, hex, url, etc.)
            
        Returns:
            Decoded string
            
        Raises:
            ValueError: If encoding type is not supported
        """
        if encoding not in self.encodings:
            raise ValueError(f"Unsupported encoding: {encoding}")
        return self.encodings[encoding]['decode'](text)
    
    def list_encodings(self) -> Dict[str, str]:
        """
        Get a list of all supported encodings with descriptions.
        
        Returns:
            Dictionary of encoding names and their descriptions
        """
        return {name: info['description'] for name, info in self.encodings.items()}


def main():
    """
    Main function that handles command-line interface.
    """
    parser = argparse.ArgumentParser(
        description='Encode and decode text using various encoding schemes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -e base64 "Hello, World!"
  %(prog)s -d base64 "SGVsbG8sIFdvcmxkIQ=="
  %(prog)s -e hex "Secret Message"
  %(prog)s --list
  echo "Hello" | %(prog)s -e base64
        """
    )
    
    parser.add_argument(
        'text',
        nargs='?',
        help='Text to encode/decode (reads from stdin if not provided)'
    )
    
    parser.add_argument(
        '-e', '--encode',
        metavar='TYPE',
        help='Encode text using specified encoding'
    )
    
    parser.add_argument(
        '-d', '--decode',
        metavar='TYPE',
        help='Decode text using specified encoding'
    )
    
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='List all available encodings'
    )
    
    args = parser.parse_args()
    
    encoder_decoder = EncoderDecoder()
    
    # List encodings if requested
    if args.list:
        print("Available encodings:")
        for name, description in encoder_decoder.list_encodings().items():
            print(f"  {name:<12} - {description}")
        return
    
    # Check that either encode or decode is specified
    if not args.encode and not args.decode:
        parser.error("Either --encode or --decode must be specified")
    
    # Check that both aren't specified
    if args.encode and args.decode:
        parser.error("Cannot specify both --encode and --decode")
    
    # Get text from argument or stdin
    if args.text:
        text = args.text
    else:
        text = sys.stdin.read().strip()
    
    try:
        if args.encode:
            result = encoder_decoder.encode(text, args.encode)
            print(result)
        else:
            result = encoder_decoder.decode(text, args.decode)
            print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
