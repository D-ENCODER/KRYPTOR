# Date    : 08/10/22 7:45 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import numpy as np


class PolybiusCipher:
    def __init__(self):
        SQUARE = [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ]
        self.SQUARE = np.array(SQUARE)
        self._plaintext = ""
        self._ciphertext = ""

    def _letter_to_numbers(self, letter):
        index1, index2 = np.where(self.SQUARE == letter)
        indexes = np.concatenate([index1 + 1, index2 + 1])
        return indexes

    def _numbers_to_letter(self, index1: int, index2: int) -> str:
        return self.SQUARE[index1 - 1, index2 - 1]

    def encrypt(self, plaintext):
        self._plaintext = plaintext.replace("j", "i").lower()
        self._ciphertext = ""
        for letter_index in range(len(self._plaintext)):
            if self._plaintext[letter_index] != " ":
                numbers = self._letter_to_numbers(self._plaintext[letter_index])
                self._ciphertext = self._ciphertext + str(numbers[0]) + str(numbers[1])
            elif self._plaintext[letter_index] == " ":
                self._ciphertext = self._ciphertext + " "

        return self._ciphertext

    def decrypt(self, ciphertext):
        self._ciphertext = ciphertext.replace(" ", "  ")
        self._plaintext = ""
        for numbers_index in range(int(len(self._ciphertext) / 2)):
            if self._ciphertext[numbers_index * 2] != " ":
                index1 = self._ciphertext[numbers_index * 2]
                index2 = self._ciphertext[numbers_index * 2 + 1]

                letter = self._numbers_to_letter(int(index1), int(index2))
                self._plaintext = self._plaintext + letter
            elif self._ciphertext[numbers_index * 2] == " ":
                self._plaintext = self._plaintext + " "

        return self._plaintext
