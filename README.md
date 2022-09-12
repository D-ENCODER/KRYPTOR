# KRYPTOR
### CAESAR CIPHER

---

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

| Plain  | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Cipher | X   | Y   | Z   | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   |

```
Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```

### PLAYFAIR CIPHER

---

The Playfair cipher or Playfair square or Wheatstone–Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair for promoting its use.

The technique encrypts pairs of letters (bigrams or digrams), instead of single letters as in the simple substitution cipher and rather more complex Vigenère cipher systems than in use. The Playfair is thus significantly harder to break since the frequency analysis used for simple substitution ciphers does not work with it. The frequency analysis of bigrams is possible, but considerably more difficult. With 600 possible bigrams rather than the 26 possible monograms (single symbols, usually letters in this context), a considerably larger cipher text is required in order to be useful. 

Using "playfair example" as the key (assuming that I and J are interchangeable), the table becomes (omitted letters in red): 

The first step of encrypting the message "hide the gold in the tree stump" is to convert it to the pairs of letters "HI DE TH EG OL DI NT HE TR EX ES TU MP" (with the null "X" used to separate the repeated "E"s). Then:

1. The pair HI forms a rectangle, replace it with BM
2. The pair DE is in a column, replace it with OD
3. The pair TH forms a rectangle, replace it with ZB
4. The pair EG forms a rectangle, replace it with XD
5. The pair OL forms a rectangle, replace it with NA
6. The pair DI forms a rectangle, replace it with BE
7. The pair NT forms a rectangle, replace it with KU
8. The pair HE forms a rectangle, replace it with DM
9. The pair TR forms a rectangle, replace it with UI
10. The pair EX (X inserted to split EE) is in a row, replace it with XM
11. The pair ES forms a rectangle, replace it with MO
12. The pair TU is in a row, replace it with UV
13. The pair MP forms a rectangle, replace it with IF

Thus, the message "hide the gold in the tree stump" becomes "BM OD ZB XD NA BE KU DM UI XM MO UV IF", which may be restructured as "BMODZ BXDNA BEKUD MUIXM MOUVI F" for ease of reading the cipher text. 

### MORSE CODE

---

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph. 
```
A = .- 
B = -... 
C =  -.-. 
D =  -.. 
E = .
F = ..-. 
G =  --.
H =  ....
I =  ..
J =  .---
K =  -.-
L =  .-..
M =  --
N =  -.
O =  ---
P =  .--.
Q =  --.-
R =  .-.
S =  ...
T =  -
U =  ..-
V =  ...-
W =  .--
X =  -..-
Y =  -.--
Z =  --..
1 =  .----
2 =  ..---
3 =  ...--
4 =  ....-
5 =  .....
6 =  -....
7 =  --...
8 =  ---..
9 =  ----.
0 =  -----
, = --..--
. = .-.-.-
? = ..--..
/ = -..-.
- = -....-
( = -.--.
) = -.--.-
```