#!/usr/bin/python3


def encode(s):
    encoded=''
    for letter in s:
        encoded+=str(ord(letter))+','
    return encoded
	
def CeasarTrans(s, key):
		encodedText=''
	for letter in s:
		encodedText += chr(ord(letter)+key)
	return encodedText

file = open('ASCII-Aufgabe.txt','r')
encodedText=''

for line in file:
    for letter in line:
        encodedText+=chr(ord(letter)+3)

print(encodedText)


print(encode('Sie haben es geschafft!'))


