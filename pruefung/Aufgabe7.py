#!/usr/bin/python3



file = open('ASCII-Aufgabe.txt','r')

content = file.read()
file.close()

out=''

for line in content:
    for c in line:
        out+=hex(ord(c))+','


print(out)
        
