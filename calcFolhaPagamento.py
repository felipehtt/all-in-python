import os
import sys
import time

sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de cálculo de folha de pagamento .\n")

salario = float(input("Informe o salário bruto: "))

beneficios = float(input("Informe o valor dos benefícios: "))

inss = 120

total = salario + beneficios - inss

os.system('cls')
sys.stdout.write("\nCalculando folha de pagamento...\n")
time.sleep(3)
os.system('cls')

if (total > 1412):
    print("\nFolha de pagamento calculada com sucesso!\n")
    print("Salário bruto: R$ {:.2f}".format(salario))
    print("Benefícios: R$ {:.2f}".format(beneficios))
    print("Desconto INSS: R$ {:.2f}".format(inss))
    print("Total a receber: R$ {:.2f}\n".format(total))
else:
    print("\nHá um erro na folha de pagamento.\n")