import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de cálculo de consumo de gasolina\n")
print("-" * 30, "\n")
distancia = float(input("Informe a distância percorrida em km: ").replace(",", "."))

consumo_medio = 12

quant_gasolina = distancia / consumo_medio

os.system('cls')
sys.stdout.write("\nCalculando quantidade de gasolina...\n")
time.sleep(3)
os.system('cls')

print(f"\nA quantidade de gasolina consumida foi: {quant_gasolina:.2f} litros\n")