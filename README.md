# KRYPTOR
[![GitHub issues](https://img.shields.io/github/issues/D-ENCODER/KRYPTOR)](https://github.com/D-ENCODER/KRYPTOR/issues)  [![GitHub forks](https://img.shields.io/github/forks/D-ENCODER/KRYPTOR)](https://github.com/D-ENCODER/KRYPTOR/network)  [![GitHub stars](https://img.shields.io/github/stars/D-ENCODER/KRYPTOR)](https://github.com/D-ENCODER/KRYPTOR/stargazers) [![GitHub license](https://img.shields.io/github/license/D-ENCODER/KRYPTOR)](https://github.com/D-ENCODER/KRYPTOR/blob/master/LICENSE)  [![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FHetjoshi1684)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FD-ENCODER%2FKRYPTOR)
### CAESAR CIPHER

---

```python
from kryptor.caesar_cipher import CaesarCipher

obj = CaesarCipher() # Default shift is 3
obj.encrypt("HELLO WORLD") # returns KHOOR ZRUOG
obj.decrypt("KHOOR ZRUOG") # returns HELLO WORLD
obj.encrypt("HELLO WORLD", 5) # returns MJQQT BTWQI
obj.decrypt("MJQQT BTWQI", 5) # returns HELLO WORLD
```

### PLAYFAIR CIPHER

---

```python
from kryptor.playfair_cipher import PlayfairCipher

obj = PlayfairCipher()
print(obj.encrypt("iamdencoder", "key")) # returns nklfalhildsw
print(obj.decrypt("nklfalhildsw", "key")) # returns iamdencoder
```

### MORSE CODE

---

```python
from kryptor.morse import Morse

obj = Morse()
print(obj.encrypt('I am Dencoder')) # returns ...  .- --  -.. . -. -.-. --- -.. . .-.
print(obj.decrypt('..  .- --  -.. . -. -.-. --- -.. . .-.')) # returns I AM DENCODER
```


### HILL CIPHER

---

```python
from kryptor.hill_cipher import HillCipher

obj = HillCipher()
print(obj.encrypt('iamdencoder', [[3, 3], [2, 5]])) # returns yqtnzvwwvawd
print(obj.decrypt('yqtnzvwwvawd', [[3, 3], [2, 5]])) # returns iamdencoderz
```

### STEGANOGRAPHY

---

1. **Hiding data behind image**

```python
from kryptor.img_steganography import ImgSteganography

obj = ImgSteganography()
obj.encrypt('I am Dencoder', 'image.png', 'output.png') # returns output.png
obj.decrypt('output.png') # returns I am Dencoder
```

2. **Hiding data behind audio**

```python
from kryptor.audio_steganography import AudioSteganography

obj = AudioSteganography()
obj.encrypt('I am Dencoder', 'audio.wav', 'output.wav') # returns output.wav
obj.decrypt('output.wav') # returns I am Dencoder
```
### VIGENERE CIPHER

---

```python
from kryptor.vigenere_cipher import VigenereCipher

obj = VigenereCipher()
print(obj.encrypt('I am Dencoder', 'key')) # returns s ek nilmsbov
print(obj.decrypt('s ek nilmsbov', 'key')) # returns i am dencoder
```
