# Date    : 14/09/22 5:39 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import string


class VigenereCipher:
    """
    def encrypt(self, plain_text, key):
    def decrypt(self, cipher_text, key):
    """
    def __init__(self):
        self._plain_text = []
        self._key = ''
        self._cipher_text = []

    def encrypt(self, plain_text, key):
        """
        :param plain_text: plain text to be encrypted (str)
        :param key: key to encrypt plain text (str)
        :return: encrypted text (str)
        """
        index = 0
        self._cipher_text = ""
        self._plain_text = plain_text.lower()
        self._key = key.lower()
        for c in self._plain_text:
            if c in string.ascii_lowercase:
                off = ord(self._key[index]) - ord('a')
                encrypt_num = (ord(c) - ord('a') + off) % 26
                encrypt = chr(encrypt_num + ord('a'))
                self._cipher_text += encrypt
                index = (index + 1) % len(self._key)
            else:
                self._cipher_text += c
        return self._cipher_text

    def decrypt(self, cipher_text, key):
        """
        :param cipher_text: cipher text to be decrypted (str)
        :param key: key to decrypt cipher text (str)
        :return: decrypted text (str)
        """
        index = 0
        self._plain_text = ""
        self._cipher_text = cipher_text.lower()
        self._key = key.lower()
        for c in self._cipher_text:
            if c in string.ascii_lowercase:
                off = ord(self._key[index]) - ord('a')
                positive_off = 26 - off
                decrypt = chr((ord(c) - ord('a') + positive_off) % 26 + ord('a'))
                self._plain_text += decrypt
                index = (index + 1) % len(self._key)
            else:
                self._plain_text += c
        return self._plain_text
