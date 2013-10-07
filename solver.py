import sys
import collections
from collections import OrderedDict
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

if (len(sys.argv) != 2):
    print "Use: python solver.py [key]"
    sys.exit(1)
key = sys.argv[1]

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

shift = []
for k in key:
	shift.append(alpha.index(k))

cipherText = open('cipher.txt','r').read()
plainText  = open('plain.txt','w')

def shiftChar(c,shift):
	pos = ord(c.lower()) - 97
	newChar = chr(97 + ((pos + shift) % 26))

	return newChar


keyIndex = 0
for c in cipherText:
	if c not in alpha:
		plainText.write(c)
	else:
		alphaPos = alpha.index(c)
		newPos = (alphaPos - shift[keyIndex]) % len(alpha)
		plainText.write(alpha[newPos])
		keyIndex += 1
		keyIndex = keyIndex % 6 # Rotate the keyIndex from 0 through 5

plainText.close()

