import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma validador de triângulos.\n")

ladoum = float(input("Informe o comprimento do primeiro lado: "))
ladodois = float(input("Informe o comprimento do segundo lado: "))
ladotres = float(input("Informe o comprimento do terceiro lado: "))

os.system('cls')
sys.stdout.write("\nVerificando se pode formar um triângulo...\n")
time.sleep(3)
os.system('cls')

if (ladoum + ladodois > ladotres) and (ladodois + ladotres > ladoum) and (ladoum + ladotres > ladodois):
    print("\nPode formar um triângulo.\n")
else:
    print("\nNão pode formar um triângulo.\n")