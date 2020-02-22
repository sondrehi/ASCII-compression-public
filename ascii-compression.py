#!/usr/bin/env python3

import time
import charprocessing as cp



# compressing:

# cp037 encoding uses 8 bits, which is necessary for the program to work:
outputFile = open("compressed.txt", "w", encoding="cp037")
inputFile = open("single-line-test.txt", "r")

if inputFile.mode == 'r':
    lines = inputFile.readlines()

    for line in lines:
        charList = list(line)
        cp.charCompress(charList, outputFile)
outputFile.close()

print('the compressed file is saved as "compressed.txt"')



# decompressing:

time.sleep(0.5)

outputFile = open("decompressed.txt", "w")
compressedFile = open("compressed.txt", "r", encoding="cp037")

if compressedFile.mode == 'r':
    lines = compressedFile.readlines()

    for line in lines:
        charList = list(line)
        cp.charDecompress(charList, outputFile)

outputFile.close()

print('the decompressed file is saved as "decompressed.txt"')






