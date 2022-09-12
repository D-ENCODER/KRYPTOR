# Date    : 10/09/22 10:31 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import string


class PlayfairCipher:
    """
    def encrypt(self, plain_text, key): to encrypt the text in Playfair Cipher\n
    def decrypt(self, cipher_text, key): to decrypt the text in Playfair Cipher
    """
    def __init__(self):
        self._plain_text = ''
        self._cipher_text = ''
        self._key = ''
        self._key_matrix = ''

    def _key_generation(self):
        main = string.ascii_lowercase.replace('j', '.')
        self._key = self._key.lower()
        self._key_matrix = ['' for i in range(5)]
        i = 0
        j = 0
        for c in self._key:
            if c in main:
                self._key_matrix[i] += c
                main = main.replace(c, '.')
                j += 1
                if j > 4:
                    i += 1
                    j = 0
        for c in main:
            if c != '.':
                self._key_matrix[i] += c

                j += 1
                if j > 4:
                    i += 1
                    j = 0

    def encrypt(self, plain_text, key):
        """
        :param plain_text: plain text to encrypt(str)
        :param key: key to encrypt the plain text(str)
        :return: encrypted text(str)
        """
        self._plain_text = plain_text
        self._key = key
        self._cipher_text = ''
        plain_text_pairs = []
        cipher_text_pairs = []
        self._key_generation()
        text = self._plain_text.replace(" ", "")
        text = text.lower()
        i = 0
        while i < len(text):
            a = text[i]
            if (i + 1) == len(text):
                b = 'x'
            else:
                b = text[i + 1]

            if a != b:
                plain_text_pairs.append(a + b)
                i += 2
            else:
                plain_text_pairs.append(a + 'x')
                i += 1

        for pair in plain_text_pairs:
            flag = False
            for row in self._key_matrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])
                    cipher_text_pair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                    cipher_text_pairs.append(cipher_text_pair)
                    flag = True
            if flag:
                continue
            for j in range(5):
                col = "".join([self._key_matrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])
                    cipher_text_pair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                    cipher_text_pairs.append(cipher_text_pair)
                    flag = True
            if flag:
                continue
            i0 = 0
            i1 = 0
            j0 = 0
            j1 = 0
            for i in range(5):
                row = self._key_matrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            cipher_text_pair = self._key_matrix[i0][j1] + self._key_matrix[i1][j0]
            cipher_text_pairs.append(cipher_text_pair)
        return "".join(cipher_text_pairs)

    def decrypt(self, cipher_text, key):
        """
        :param cipher_text: cipher text to decrypt (str)
        :param key: key to decrypt the cipher text (str)
        :return: decrypted text (str)
        """
        self._cipher_text = cipher_text.lower()
        self._key = key
        self._plain_text = ''
        plain_text_pairs = []
        cipher_text_pairs = []
        self._key_generation()
        i = 0
        while i < len(self._cipher_text):
            a = self._cipher_text[i]
            b = self._cipher_text[i + 1]
            cipher_text_pairs.append(a + b)
            i += 2
        for pair in cipher_text_pairs:
            flag = False
            for row in self._key_matrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])
                    plain_text_pair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                    plain_text_pairs.append(plain_text_pair)
                    flag = True
            if flag:
                continue
            for j in range(5):
                col = "".join([self._key_matrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])
                    plain_text_pair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                    plain_text_pairs.append(plain_text_pair)
                    flag = True
            if flag:
                continue
            i0 = 0
            i1 = 0
            j0 = 0
            j1 = 0
            for i in range(5):
                row = self._key_matrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            plain_text_pair = self._key_matrix[i0][j1] + self._key_matrix[i1][j0]
            plain_text_pairs.append(plain_text_pair)
        return "".join(plain_text_pairs)
