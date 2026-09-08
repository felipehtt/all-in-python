import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de cálculo de bônus anual.\n")

salario = float(input("Informe o salário mensal: "))
tempo_casa = float(input("Informe o tempo de casa (em anos): "))
nota = float(input("Informe a nota do funcionário (de 0 a 10): "))

os.system('cls')
sys.stdout.write("\nCalculando bônus anual...\n")
time.sleep(3)
os.system('cls')

if tempo_casa >= 1:
    if nota >= 8:
        bonus = salario * 0.2
        print(f"\nParabéns! Você recebeu um bônus anual de R${bonus:.2f}.\n")
    else:
        bonus = salario * 0.1
        print(f"\nVocê recebeu um bônus anual de R${bonus:.2f}.\n")
else:
    bonus = 0
    print("\nVocê não tem direito a bônus anual.\n")