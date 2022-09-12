# Date    : 11/09/22 9:27 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

class Morse:
    """
        def encrypt(self, plain_text): to encrypt the text in Morse Code\n
        def decrypt(self, encrypted_text): to decrypt the text in Morse Code
    """
    def __init__(self):
        self._morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
            '-': '-....-', '(': '-.--.', ')': '-.--.-'
        }
        self._morse_inv = {v: k for k, v in self._morse.items()}
        self._plain_text = ''
        self._encrypted_text = ''

    def encrypt(self, plain_text):
        """
        :param plain_text: Plain text to be encrypted (str)
        :return: Encrypted text (str)
        """
        self._plain_text = plain_text.upper()
        self._encrypted_text = ''
        for letter in self._plain_text:
            if letter != ' ':
                self._encrypted_text += self._morse[letter] + ' '
            else:
                self._encrypted_text += ' '
        return self._encrypted_text

    def decrypt(self, encrypted_text):
        """
        :param encrypted_text: Encrypted text to be decrypted (str)
        :return: Decrypted text (str)
        """
        self._encrypted_text = encrypted_text
        self._encrypted_text += ' '
        self._plain_text = ''
        temp = ''
        i = 0
        for letter in self._encrypted_text:
            if letter != ' ':
                i = 0
                temp += letter
            else:
                i += 1
                if i == 2:
                    self._plain_text += ' '
                else:
                    self._plain_text += self._morse_inv[temp]
                    temp = ''
        return self._plain_text
