#!/usr/bin/python3

# Algorithmen zur Bestimmung eines Bitmusters (Binärdarstellung)
# Autor: Gregor Lüdi, 2.9.2014


import math

def binAlgInt1(i,stellen):
    bitpat=[]
    bitlaenge =int( math.log(i)/math.log(2)+1)
    s = stellen - bitlaenge
    while i>0:
        bitpat.append(i%2)
        i//=2
    # der algorithmus schreibt erst das msb, bitpattern muss gedreht werden
    bitpat.reverse()
    return [0]*s+bitpat

def binAlgInt2(i,stellen):
    bitpat=[]
    bitlaenge =int(math.log(i)/math.log(2)+1)
    s = stellen - bitlaenge
    zweierpotenzen = [2**x for x in range(bitlaenge)[::-1]]
    #erstellt eine absteigende Liste von Zweierpotenzen
    for z in zweierpotenzen:
        if i>=z:
            bitpat.append(1)
            i=i-z
        else:
            bitpat.append(0)
    return [0]*s+bitpat

def binAlgFrac(z,stellen):
    bitpat=[]
    z*=2
    for i in range(stellen):
        if z<1:
            bitpat.append(0)
        else:
            bitpat.append(1)
            z=z-1
        z*=2
    return bitpat

def binAlgSignInt(z,stellen):
    if z<0:
        sign=1
        bitpat =binAlgInt1(-z,stellen-1)
        bitpat = binInvert(bitpat)
        bitpat = binSum(bitpat,[1])
        return [1]+bitpat
    else:
        return [0]+binAlgInt1(z,stellen-1)

def binInvert(muster):
    bitpat=[]
    for bit in muster:
        if bit ==0:
            bitpat.append(1)
        else:
            bitpat.append(0)
    return bitpat

def dezBin(bitpat):
    stellen = len(bitpat)
    pow2 = [2**x for x in range(stellen)[::-1]]
    summe=0
    for i in range(stellen):
        summe+=bitpat[i]*pow2[i]
    return summe

def binSum(a,b):
    if len(a) >=len(b):
        stellen = len(a)
        b = [0]*(stellen-len(b))+b
    else:
        stellen = len(b)
        a = [0]*(stellen-len(a))+a
    bitpat=[0]*stellen
    carry = 0
    for index in range(len(a))[::-1]:
        sum = a[index]+b[index]+carry
        if sum ==0:
            bitpat[index]=0
            carry=0
        elif sum ==1:
            bitpat[index]=1
            carry=0
        elif sum ==2:
            bitpat[index]=0
            carry=1
        else:
            bitpat[index]=1
            carry=1
    if carry ==1:
        return 'Carry !'
    return bitpat

def binFloat(zahl,stellen):
	#bestimmung des bitmusters für die Mantisse
    ganz = int(zahl)
    gebrochen = zahl-ganz
    if ganz == 0:
        stellenVorDemKomma =1
        bitpattern =[0]
    else:
        stellenVorDemKomma = int(math.log(ganz)/math.log(2)+1)
        bitpattern =binAlgInt1(ganz,stellenVorDemKomma)
    # hier wäre der Dezimalpunkt  bitpattern+='.'
    bitpattern=bitpattern +['.']+binAlgFrac(gebrochen,stellen-stellenVorDemKomma)
    return bitpattern

# ---------------------------------------------------------
# es fehlt noch eine Prozedur welche die Dezimalpunktdarstellung richtig macht:
# vorzeichen, exponentn und mantisse
# ---------------------------------------------------------

def main():
    zahl = float(input('Geben Sie eine Zahl ein: '))
    stellen = int(input('Geben Sie die Stellenzahl ein: '))    
    bit=[]
	
    if zahl.is_integer():
        if zahl>0.0:
            bit=binAlgInt1(int(zahl),stellen)
        else:
            bit=binAlgSignInt(int(zahl),stellen)
    else:
        bit=binFloat(zahl,stellen)
		
    print(''.join(str(x) for x in bit))

    input()

if __name__=='__main__':main()
