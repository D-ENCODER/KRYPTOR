# Date    : 10/09/22 9:29 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

class CaesarCipher:
    """
    def encrypt(self, plain_text, key): to encrypt the text in Caesar Cipher\n
    def decrypt(self, cipher_text, key): to decrypt the text in Caesar Cipher
    """

    def __init__(self):
        self._plain_text = ''
        self._key = 0
        self._cipher_text = ''

    def encrypt(self, plain_text, key=3):
        """
        :param plain_text: text to encrypt in caesar cipher (str)
        :param key: _key to encrypt the text (int) (optional)
        :return: encrypted text (str)
        """
        self._plain_text = plain_text
        self._key = key
        self._cipher_text = ''
        for char in plain_text:
            if char == " ":
                self._cipher_text += char
            elif char.isupper():
                self._cipher_text += chr((ord(char) + key - 65) % 26 + 65)
            else:
                self._cipher_text += chr((ord(char) + key - 97) % 26 + 97)
        return self._cipher_text

    def decrypt(self, cipher_text, key=3):
        """
        :param cipher_text: cipher text to decrypt (str)
        :param key: _key to decrypt the text (int) (optional)
        :return: decrypted text (str)
        """
        self._cipher_text = cipher_text
        self._key = key
        self._plain_text = ''
        for char in cipher_text:
            if char == " ":
                self._plain_text += char
            elif char.isupper():
                self._plain_text += chr((ord(char) - key - 65) % 26 + 65)
            else:
                self._plain_text += chr((ord(char) - key - 97) % 26 + 97)
        return self._plain_text

