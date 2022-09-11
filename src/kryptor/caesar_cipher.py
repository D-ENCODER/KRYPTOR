# Date    : 10/09/22 9:29 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

class CaesarCipher:
    """
    def encrypt(self): to encrypt the text in caesar cipher\n
    def decrypt(self): to decrypt the text in caesar cipher
    """
    @staticmethod
    def encrypt(text, key):
        """
        :param text: text to encrypt in caesar cipher (str)
        :param key: _key to encrypt the text (int)
        :return: encrypted text (str)
        """
        cipher_text = ""
        for char in text:
            if char == " ":
                cipher_text += char
            elif char.isupper():
                cipher_text += chr((ord(char) + key - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(char) + key - 97) % 26 + 97)
        return cipher_text

    @staticmethod
    def decrypt(cipher_text, key):
        """
        :param cipher_text: cipher text to decrypt (str)
        :param key: _key to decrypt the text (int)
        :return: decrypted text (str)
        """
        plain_text = ""
        for char in cipher_text:
            if char == " ":
                plain_text += char
            elif char.isupper():
                plain_text += chr((ord(char) - key - 65) % 26 + 65)
            else:
                plain_text += chr((ord(char) - key - 97) % 26 + 97)
        return plain_text
