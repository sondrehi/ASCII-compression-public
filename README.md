# ASCII compression
A proof-of-concept python program for compressing ASCII text.

This program is intended to save space for files in plain ASCII text.
This is achieved by using the most popular characters in the english language.
One single <a href="https://en.wikipedia.org/wiki/American_National_Standards_Institute">ANSI/ASCII</a> character will use one byte of storage on a computer. If two characters in a row are one of the most popular characters, they will be merged together to the size of one byte.
This means that if, for instance, a user were to write a text comprising of only popular characters then the compressed file will be 
half as big as a regular text file.
