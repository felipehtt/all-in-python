import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de aprovação de empréstimo .\n")

salario = float(input("Informe o salário bruto: "))
valor_emprestimo = float(input("Informe o valor do empréstimo: "))
quant_meses = int(input("Informe a quantidade de meses para pagar: "))

parcela = valor_emprestimo / quant_meses

salario_disponivel = salario * 0.3

os.system('cls')
sys.stdout.write("\nCalculando aprovação de empréstimo...\n")
time.sleep(3)
os.system('cls')

if (parcela > salario_disponivel):
    print("\nEmpréstimo não aprovado.\n")
    print(f"O valor da parcela (R$ {parcela:.2f}) é maior que 30% do seu salario (R$ {salario_disponivel:.2f}).\n")
else:
    print("\nEmpréstimo aprovado!\n")
    print(f"O valor da parcela (R$ {parcela:.2f}) é menor que 30% do seu salario (R$ {salario_disponivel:.2f}).\n")