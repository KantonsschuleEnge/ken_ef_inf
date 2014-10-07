#
#   autor: gregor luedi
#   date: 6.10.2014
#


def text2hex(s):
    hextext=''
    for letter in s:
        hextext=hextext+'\\'+hex(ord(letter))

    return hextext


def hex2text(s):
    hexlist = s.split('\\0x')
    text = ''
    for item in hexlist[1:]:
        text =text+chr(int(item))

    return text


print(text2hex('gregor'))
print(hex2text(text2hex('gregor')))
