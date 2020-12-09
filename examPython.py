from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)
from random import randrange


tableauMot = ["WEBCAM", "ABOLIR","PIMENT","SAFARI","TUYAUX", "GARANT", "NACRES", "ACCORD", "EFFORT", "GAGNER"]
numero = randrange(len(tableauMot))
print(numero)
print(tableauMot[numero])
mot = tableauMot[numero]
propositionMot = input('essayez de trouver le mot ')
propositionMot = propositionMot.upper()
lettre = 0
tableauLettreBonnePlace = ["" ,"" ,"" , "", "","" ]


for i in range (0,6): 
    for x in range (0,6) :
        if mot[i] == propositionMot[x] : #parcours les chaînes de caractères mot et proposition
            lettre=lettre + 1
            if i == x : 
                tableauLettreBonnePlace[x] = 1 #crée un tableau avec les emplacements des lettres à la bonne place identifiées par un 1
            else :
                    tableauLettreBonnePlace[x] = 0
        else:
                lettre = lettre

for i in range (0,6): 
    if tableauLettreBonnePlace[i] == 1: 
        print(Back.RED + propositionMot[i], 'est à la bonne place') #si la lettres est au bonne endroit, elle est affichée en rouge
           
    

print('il y a', lettre ,'lettre correspondante' )
print(propositionMot)
input()