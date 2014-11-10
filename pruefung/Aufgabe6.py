#!/usr/bin/python3


file = open('code.txt','r')

content = file.read()

werte = content.split(',')

for wert in werte:
    print(chr(int(wert)),end='')
