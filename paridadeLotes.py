import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de paridade de lotes.\n")

numLote = int(input("Informe o número do lote: "))

numLotePar = numLote % 2

os.system('cls')
sys.stdout.write("\nVerificando lote...\n")
time.sleep(3)
os.system('cls')

if (numLotePar == 0):
    print("\nO lote {} é par.\n".format(numLote))
else:
    print("\nO lote {} é ímpar.\n".format(numLote))