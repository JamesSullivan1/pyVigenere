pyVigenere
========
Vigenere Cipher cracking made easy!

-----
frequency.py :
  Uses matplotlib to generate a set of graphs counting the relative frequency of occurance of every alphabetic character in a given text.
    These graphs can be used to perform trivial visual frequency analysis on the ciphertext to ascertain a key.
    Currently hardcoded to keys of length 6 (As was in this particular instance). May modify this in the future.

-----
solver.py : 
  Performs a Vigenere Decryption given a key and a ciphertext.



-----
Future:

-Modify frequency.py to work with any keylength (or possibly to analyze a range of keylengths)
