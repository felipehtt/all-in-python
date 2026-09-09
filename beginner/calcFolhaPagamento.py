import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de cálculo de folha de pagamento .\n")

salario = float(input("Informe o salário bruto: "))

beneficios = float(input("Informe o valor dos benefícios: "))

inss = salario * 0.08

total = salario + beneficios - inss

os.system('cls')
sys.stdout.write("\nCalculando folha de pagamento...\n")
time.sleep(3)
os.system('cls')

if (total > 1412):
    print("\nFolha de pagamento calculada com sucesso!\n")
    print(f"Salário bruto: R$ {salario:.2f}")
    print(f"Benefícios: R$ {beneficios:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Total a receber: R$ {total:.2f}\n")
else:
    print("\nHá um erro na folha de pagamento.\n")