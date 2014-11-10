#!/usr/bin/python3
# logische Verknüpfungen

#   und:    &
#   oder:   |
#   xor:    ^

def logArg(x,y):
    return x&y|(x^(x|y))


def logArg3(x,y,z):
    return x&y|(x^(x|z))

def truthTable():
    print("x\t\ty\t\tz\t\te")
    print(60*'-')
    for x in [0,1]:
        for y in [0,1]:
            for z in [0,1]:
                e = logArg3(x,y,z)
                print("{}\t|\t{}\t|\t{}\t|\t {}".format(x,y,z,e))
def halfAdder(x,y):
    return [x&y,(x^y)]

def fullAdder(a,b,c):
    x = halfAdder(a,b)
    y = halfAdder(x[1],c)
    return [y[1],x[0]|y[0]]


#print("x\t|\ty\t|\tz")
#print(40*'-')
"""for x in[1,0]:
    for y in [1,0]:
        z = logArg(x,y)
        print("{}\t|\t{}\t|\t{}".format(x,y,z))
print()
"""
truthTable()

print(fullAdder(1,0,0))

        

