#!/usr/bin/python3

# author    gregor luedi
# filename  wahrheitstafel.py

#	logisches und:  and       &			x and y
#	logisches oder:	or        |			x or y
#	logisches entweder oder ^    gibt es nur bitweise und nicht als funktion
#	logisches nicht: not()

# erstellen der Liste mit den beiden Wahrheitswerten
booleanList = [True,False] # oder auch [1,0]

# funktion welche einen logischen Ausdruck berechnet
def logAusdruck(x,y):
<<<<<<< HEAD:wahrheitstafel.py
    return (x^y) | (not(x) and y)
=======
    return (not( x) or y)
>>>>>>> origin/master:Testpruefung/wahrheitstafel.py

def logAusdruck2(x,y):
    return (not((x or not(y)) and x) or y)

# drucken der ueberschrift der tabelle
print('x\t|\ty\t|\tz')
print(50*'-')
#jede kombination zweier wahrheitwert 
for x in booleanList:
    for y in booleanList:
	# drucken einer tabelle in der form x | y | z-wert
        print('{}\t|\t{}\t|\t{}'.format(x,y,logAusdruck(x,y)))

<<<<<<< HEAD:wahrheitstafel.py

input()
=======
>>>>>>> origin/master:Testpruefung/wahrheitstafel.py
