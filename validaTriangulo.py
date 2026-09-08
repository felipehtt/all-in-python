import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma validador de triângulos.\n")

lado_um = float(input("Informe o comprimento do primeiro lado: "))
lado_dois = float(input("Informe o comprimento do segundo lado: "))
lado_tres = float(input("Informe o comprimento do terceiro lado: "))

os.system('cls')
sys.stdout.write("\nVerificando se pode formar um triângulo...\n")
time.sleep(3)
os.system('cls')

if (lado_um + lado_dois > lado_tres) and (lado_dois + lado_tres > lado_um) and (lado_um + lado_tres > lado_dois):
    print(f"\nPode formar um triângulo.\n")
else:
    print(f"\nNão pode formar um triângulo.\n")