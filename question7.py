import sys
import collections
from collections import OrderedDict
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

cipherText = open('cipher.txt','r').read()
charFreq = open("Char_Frequency.txt", "w")

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Creates six dictionaries associating each letter to their frequency of occurance (default 0)
splitTextFrequency = [{},{},{},{},{},{}]
for i in splitTextFrequency:
  for char in alpha:
    i[char] = 0


# Iterates through ciphertext and counts the frequency of each letter (rotating through each of the above dictionaries each character)
keyIndex = 0
for c in cipherText:
  if c not in alpha:
    del(c)
  else:
    splitTextFrequency[keyIndex][c] += 1 # Increment the character count in the particular dictionary
    keyIndex += 1
    keyIndex = keyIndex % 6 # Rotate the keyIndex from 0 through 5


# Utility function to add up the total characters in a dictionary associating characters to their count
def total(charCount):
  length = 0
  for char in charCount:
    length += charCount[char]
  return length

# Store total character count of each dictionary
totalChar = [
total(splitTextFrequency[0]),
total(splitTextFrequency[1]),
total(splitTextFrequency[2]),
total(splitTextFrequency[3]),
total(splitTextFrequency[4]),
total(splitTextFrequency[5])
]

# Plots will go into a PDF file
plots = PdfPages('freqPlots.pdf')

# Change all counts to a relative frequency and write to file.
# Also creates graphs for each key index.
for kUnordered in splitTextFrequency:
  index = splitTextFrequency.index(kUnordered)
  k = OrderedDict(sorted(kUnordered.items()))
  charFreq.write(str(index) + " - Frequencies of occurance \n")
  index = splitTextFrequency.index(k)
  for char in k:
    k[char] = 100 * float(k[char]) / totalChar[index] # Convert frequency to % format
    print k[char]
    charFreq.write(char + "  " + "%.2f" % k[char] + "\n")
  charFreq.write("----------\n\n")

  fig = plt.figure()
  plt.title("Key Index %d" % index)
  plt.bar(range(len(k)),k.values())
  plt.xticks(range(len(k)), k.keys())
  plt.xlabel("Char")
  plt.ylabel("Frequency (%)")
  plt.ylim([0,20])
  fig.savefig(plots, format='pdf')


# Sample frequencies -  source: http://www.cryptograms.org/letter-frequencies.php
sampleUnordered = {'A':8.17,'B':1.49,'C':3.78,'D':4.25,'E':12.70,'F':2.22,'G':2.02,'H':6.09,'I':6.97,'J':0.15,
'K':0.77,'L':4.03,'M':2.41,'N':6.75,'O':7.51,'P':1.93,'Q':0.01,'R':5.99,'S':6.33,'T':9.06,'U':2.76,'V':0.98,'W':2.36,'X':0.15,'Y':1.97,'Z':0.07}
sampleFrequencies = OrderedDict(sorted(sampleUnordered.items()))

fig = plt.figure()
plt.title("Sample Data - http://www.cryptograms.org/letter-frequencies.php")
plt.bar(range(len(sampleFrequencies)),sampleFrequencies.values())
plt.xticks(range(len(sampleFrequencies)), sampleFrequencies.keys())
plt.xlabel("Char")
plt.ylabel("Frequency (%)")
plt.ylim([0,20])
fig.savefig('samplePlot.pdf')

plots.close()