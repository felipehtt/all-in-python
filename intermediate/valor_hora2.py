import os, sys, time

def calcular_valor_hora(quant_dias, horas_dia, salario):
    valor_hora = salario / (horas_dia * quant_dias)
    return valor_hora

try:

    os.system('cls')
    sys.stdout.write("\nCarregando programa...\n")
    time.sleep(2)
    os.system('cls')

    print("\nPrograma de calculo de valor por hora trabalhada.\n")

    quant_dias = int(input("Informe quantos dias você trabalha por mês: "))
    horas_dia = float(input("Informe quantas horas você trabalha por dia: "))
    salario = float(input("Informe quanto você recebe por mês: "))

    valor_hora = calcular_valor_hora(quant_dias, horas_dia, salario)

    os.system('cls')
    sys.stdout.write("\nCalculando valor por hora trabalhada...")
    time.sleep(3)
    os.system('cls')

    print(f"\nO valor que você recebe por hora trabalhada é de R$ {valor_hora:.2f}\n")

except ValueError:
    print("\nErro: Por favor, insira apenas números válidos.\n")