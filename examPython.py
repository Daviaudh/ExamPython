from colorama import init
init()
from colorama import Fore, Back, Style

from random import randrange


tableauMot = ["WEBCAM", "ABOLIR","PIMENT","SAFARI","TUYAUX", "GARANT", "NACRES", "ACCORD", "EFFORT", "GAGNER"]
numero = randrange(len(tableauMot))
print(numero)
print(tableauMot[numero])
mot = tableauMot[numero]
propositionMot = input('essayez de trouver le mot ')
propositionMot = propositionMot.upper()
lettre = 0
for i in range (0,6):
    for x in range (0,6) :
        if mot[i] == propositionMot[x] :
            
            lettre=lettre + 1
            
        else:
                lettre = lettre
                
print('il y a', lettre ,'lettre correspondante' )

input()