# Date    : 12/09/22 8:18 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import numpy as np


class HillCipher:
    """
        def encrypt(self): to encrypt the text in Hill Cipher\n
        def decrypt(self): to decrypt the text in Hill Cipher
    """

    def __init__(self):
        self._key = []
        self._cipher_text = ''
        self._plain_text = ''

    def _message_matrix(self, s):
        """
            This function will convert the message into matrix
        :param s: message (string)
        :return: matrix (list)
        """
        n = len(self._key)
        s = s.replace(" ", "")
        s = s.lower()
        final_matrix = []
        if len(s) % n != 0:
            while len(s) % n != 0:
                s = s + 'z'
        for k in range(len(s) // n):
            message_matrix = []
            for i in range(n):
                sub = []
                for j in range(1):
                    sub.append(ord(s[i + (n * k)]) - ord('a'))
                message_matrix.append(sub)
            final_matrix.append(message_matrix)
        return final_matrix

    @staticmethod
    def _getCofactor(mat, temp, p, q, n):
        """
            This function will get the cofactor of the matrix
        :param mat: matrix (list)
        :param temp: temporary matrix (list)
        :param p: row (int)
        :param q: column (int)
        :param n: size of matrix (int)
        :return: None
        """
        i = 0
        j = 0
        for row in range(n):
            for col in range(n):
                if row != p and col != q:
                    temp[i][j] = mat[row][col]
                    j += 1
                    if j == n - 1:
                        j = 0
                        i += 1

    def _determinantOfMatrix(self, mat, n):
        """
            This function will calculate the determinant of the matrix
        :param mat: matrix (list)
        :param n: size of matrix (int)
        :return: determinant (int)
        """
        D = 0
        if n == 1:
            return mat[0][0]
        temp = [[0 for _ in range(n)]
                for _ in range(n)]
        sign = 1
        for f in range(n):
            self._getCofactor(mat, temp, 0, f, n)
            D += (sign * mat[0][f] *
                  self._determinantOfMatrix(temp, n - 1))
            sign = -sign
        return D

    def _isInvertible(self, mat, n):
        """
            This function will check whether the matrix is invertible or not
        :param mat: matrix (list)
        :param n: size of matrix (int)
        :return: True or False (bool)
        """
        if self._determinantOfMatrix(mat, n) != 0:
            return True
        else:
            return False

    @staticmethod
    def _multiply_and_convert(key, message):
        """
            This function will multiply the key and message matrix and convert the result into character
        :param key: key matrix (list)
        :param message: message matrix (list)
        :return: final matrix (list)
        """
        res_num = [[0 for _ in range(len(message[0]))]
                   for _ in range(len(key))]

        for i in range(len(key)):
            for j in range(len(message[0])):
                for k in range(len(message)):
                    res_num[i][j] += key[i][k] * message[k][j]

        res_alpha = [['' for _ in range(len(message[0]))]
                     for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(message[0])):
                res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)
        return res_alpha

    @staticmethod
    def _modInverse(a, m):
        """
            This function will calculate the modular inverse of the matrix
        :param a: matrix (list)
        :param m: size of matrix (int)
        :return: modular inverse (list)
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return 1

    def _method(self, a, m):
        """
            This function will calculate the modular inverse of the matrix
        :param a: matrix (list)
        :param m: size of matrix (int)
        :return: modular inverse (list)
        """
        if a > 0:
            return a % m
        else:
            k = (abs(a) // m) + 1
        return self._method(a + k * m, m)

    def encrypt(self, plain_text, key):
        """
        :param plain_text: plain text (string)
        :param key: key (list)
        :return: cipher text (string)
        """
        self._cipher_text = ''
        self._plain_text = plain_text
        self._key = key
        if self._isInvertible(self._key, len(self._key)):
            pass
        else:
            print("NOTE:- THE KEY IS NOT INVERTIBLE (CAN'T BE DECRYPTED)")
        message = self._message_matrix(self._plain_text)
        final_message = ''
        for i in message:
            sub = self._multiply_and_convert(self._key, i)
            for j in sub:
                for k in j:
                    final_message += k
        return final_message

    def decrypt(self, cipher_text, key):
        """
        :param cipher_text: cipher text (string)
        :param key: key (list)
        :return: plain text (string)
        """
        self._cipher_text = cipher_text
        self._key = key
        self._plain_text = ''
        A = np.array(self._key)
        det = np.linalg.det(A)
        adjoint = det * np.linalg.inv(A)
        if det != 0:
            convert_det = self._modInverse(int(det), 26)
            adjoint = adjoint.tolist()
            for i in range(len(adjoint)):
                for j in range(len(adjoint[i])):
                    adjoint[i][j] = round(adjoint[i][j])
                    adjoint[i][j] = self._method(adjoint[i][j], 26)
            adjoint = np.array(adjoint)
            inverse = convert_det * adjoint
            inverse = inverse.tolist()
            for i in range(len(inverse)):
                for j in range(len(inverse[i])):
                    inverse[i][j] = inverse[i][j] % 26
            message = self._message_matrix(self._cipher_text)
            plain_text = ''
            for i in message:
                sub = self._multiply_and_convert(inverse, i)
                for j in sub:
                    for k in j:
                        plain_text += k
            return plain_text
        else:
            print("NOTE:- THE KEY IS NOT INVERTIBLE (CAN'T BE DECRYPTED)")
