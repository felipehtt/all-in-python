import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de paridade de lotes.\n")

num_lote = int(input("Informe o número do lote: "))

num_lote_par = num_lote % 2

os.system('cls')
sys.stdout.write("\nVerificando lote...\n")
time.sleep(3)
os.system('cls')

if (num_lote_par == 0):
    print(f"\nO lote {num_lote} é par.\n")
else:
    print(f"\nO lote {num_lote} é ímpar.\n")