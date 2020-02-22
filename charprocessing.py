#!/usr/bin/env python3

firstCommonChars = ["e", "a", "r", "i", "o", "t", "n", " "] # 3 bits
secondCommonChars = ["e", "a", "r", "i", "o", "t", "n", " ", "s", "l", "c", "u", "d", "p", "m", "v"] # 4 bits

def charCompress(charList, outputFile):

    length = len(charList)
    j = 0

    while j < length: # for char in line:

        if charList[j] in firstCommonChars: # if the character is one of the popular characters:
            if (j + 1) != length:
                if charList[j + 1] in secondCommonChars: # if the next character is one of the popular characters:

                    # the two characters will be replaced with a non-ascii character

                    firstIndex = 0
                    i = 0
                    while i < 8:
                        if charList[j] == firstCommonChars[i]:
                            firstIndex = i
                        i += 1

                    secondIndex = 0
                    i = 0
                    while i < 16:
                        if charList[j + 1] == secondCommonChars[i]:
                            secondIndex = i
                        i += 1

                    # get 3 bits from the first index:
                    firstIndexBin = "{:03b}".format(firstIndex)

                    # get 4 bits from the second index:
                    secondIndexBin = "{:04b}".format(secondIndex)

                    mergedCharBin = '1' + firstIndexBin + secondIndexBin
                    mergedChar = chr(int(mergedCharBin, 2))

                    outputFile.write(mergedChar)

                    j += 2
                    continue

        outputFile.write(charList[j])
        j += 1


def charDecompress(charList, outputFile):
    
    length = len(charList)
    j = 0

    while j < length: # for char in line:
        
        charInt = ord(charList[j])
        charStr = "{:08b}".format(charInt) # reformat to an 8 character string sequence
        
        if charStr[0] == '1': # if the first binary number is 1 it is a merged char:
            
            firstIndexBin = charStr[1:4]
            secondIndexBin = charStr[4:8]
            
            firstChar = firstCommonChars[int(firstIndexBin, 2)]
            secondChar = secondCommonChars[int(secondIndexBin, 2)]
            
            outputFile.write(firstChar + secondChar)
            
            j += 1
            continue
        
        outputFile.write(charList[j])
        j += 1
    
    
    
    
    
    
    