# Date    : 14/09/22 11:06 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import wave


class AudioStenganography:
    """
    def encrypt(self, data, audio_path, encrypted_audio_path='song_embedded.wav'):
    def decrypt(self, audio_path):
    """

    def __init__(self):
        self._data = ''
        self._audio_path = ''
        self._encrypted_audio_path = ''
        self._decrypted_data = ''

    def encrypt(self, data, audio_path, encrypted_audio_path='song_embedded.wav'):
        """
        :param data: data to be embedded (str)
        :param audio_path: path of audio file(only .wav) (str)
        :param encrypted_audio_path: path of encrypted audio file(only .wav) (str) (optional)
        :return: None (encrypted audio file is saved)
        """
        self._data = data
        self._audio_path = audio_path
        self._encrypted_audio_path = encrypted_audio_path
        audio = wave.open(self._audio_path, 'rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        self._data = self._data + int((len(frame_bytes) - (len(self._data) * 8 * 8)) / 8) * '#'
        bits = list(
            map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in self._data])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        with wave.open(self._encrypted_audio_path, 'wb') as fd:
            fd.setparams(audio.getparams())
            fd.writeframes(frame_modified)
        audio.close()

    def decrypt(self, audio_path):
        """
        :param audio_path: path of audio file(only .wav) (str)
        :return: data embedded in audio file (str)
        """
        self._data = ''
        self._audio_path = audio_path
        song = wave.open(self._audio_path, 'rb')
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(
            int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
        self._data = string.split("###")[0]
        song.close()
        return self._data
