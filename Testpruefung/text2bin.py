#!/usr/bin/python3

#   author  gregor luedi
#   filen   text2bin.py

# Lösung der Aufgabe 'Ishmael'

#daten aus einer datei lesen:
file = open('testdaten.txt','r')
#text = file.read() oder zeilenweise:

for line in file:
    for letter in line:
        print(format(ord(letter),'#02x'),end=',')



# oder den text direkt laden
"""
text = 'Call me Ishmael ...'

for letter in text:
    print(format(ord(letter),'#010b'))

"""

