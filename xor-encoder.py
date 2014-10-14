#!/usr/bin/python3


shellcode=(b'\x9b\xfa')

encoded=''
encoded2=''

print(shellcode)

print('Encoded shellcode ... ')

for x in bytearray(shellcode):
    y=x^0xAA
    encoded +='\\x'
    encoded += '%02x'% y

    encoded2 += '0x'
    encoded2 += '%02x,' %y

print(encoded)
print(encoded2)
print('Len: %d' %len(bytearray(shellcode)))

