# Date    : 13/09/22 6:11 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import cv2
import math


class ImgStenganography:
    """
    def encrypt(self, data, image_path): to encrypt the data in image\n
    def decrypt(self, img_path): to decrypt the data from image
    """
    def __init__(self):
        self._message = ''

    def encrypt(self, data, image_path, new_img_path="encrypt_data_image.png"):
        """
        :param data: data to be encrypted
        :param image_path: path of image (str)
        :param new_img_path: path of new image (str) (optional)
        :return: None (image is saved in the same directory)
        """
        self._message = data
        img = cv2.imread(image_path)
        self._message = [format(ord(i), '08b') for i in data]
        _, width, _ = img.shape
        PixReq = len(self._message) * 3
        RowReq = PixReq / width
        RowReq = math.ceil(RowReq)
        count = 0
        charCount = 0
        for i in range(RowReq + 1):
            while count < width and charCount < len(data):
                char = self._message[charCount]
                charCount += 1
                for index_k, k in enumerate(char):
                    if ((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (
                            k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                        img[i][count][index_k % 3] -= 1
                    if index_k % 3 == 2:
                        count += 1
                    if index_k == 7:
                        if charCount * 3 < PixReq and img[i][count][2] % 2 == 1:
                            img[i][count][2] -= 1
                        if charCount * 3 >= PixReq and img[i][count][2] % 2 == 0:
                            img[i][count][2] -= 1
                        count += 1
            count = 0
        cv2.imwrite(new_img_path, img)

    def decrypt(self, img_path):
        """
        :param img_path: path of image (str)
        :return: decrypted data (str)
        """
        self._message = ''
        img = cv2.imread(img_path)
        data = []
        stop = False
        for _, i in enumerate(img):
            i.tolist()
            for index_j, j in enumerate(i):
                if index_j % 3 == 2:
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    if bin(j[2])[-1] == '1':
                        stop = True
                        break
                else:
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    data.append(bin(j[2])[-1])
            if stop:
                break
        temp_message = []
        for i in range(int((len(data) + 1) / 8)):
            temp_message.append(data[i * 8:(i * 8 + 8)])
        temp_message = [chr(int(''.join(i), 2)) for i in temp_message]
        self._message = str(''.join(temp_message))
        return self._message
