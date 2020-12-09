from colorama import init
init()
from colorama import Fore, Back, Style

from random import randrange


tableauMot = ["WEBCAM", "ABOLIR","PIMENT","SAFARI","TUYAUX", "GARANT", "NACRES", "ACCORD", "EFFORT", "GAGNER"]
numero = randrange(len(tableauMot))
print(numero)
print(tableauMot[numero])

proposition = input('essayez de trouver le mot ')

while proposition != tableauMot[numero]:
    print('vous avez raté essayez encore ')
    