import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de calculo de valor por hora trabalhada.\n")

quantDias = float(input("Informe quantos dias você trabalha por mês: "))
horasDia = float(input("Informe quantas horas você trabalha por dia: "))
salario = float(input("Informe quanto você recebe por mês: "))

valorHora = salario / (horasDia * quantDias)

os.system('cls')
sys.stdout.write("\nCalculando valor por hora trabalhada...")
time.sleep(3)
os.system('cls')

print("\nO valor que você recebe por hora trabalhada é de R$ {:.2f}\n".format(valorHora))