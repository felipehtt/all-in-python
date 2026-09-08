import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de verificação de orçamento.\n")
monitor = float(input("Informe o valor do monitor: "))

total = monitor * 3

os.system('cls')
print("\nVerificando se está dentro do orçamento...\n")
time.sleep(3)
os.system('cls')

print(total <= 2500)