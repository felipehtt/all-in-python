import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de aprovação de empréstimo .\n")

salario = float(input("Informe o salário bruto: "))
valorEmprestimo = float(input("Informe o valor do empréstimo: "))
quantMeses = int(input("Informe a quantidade de meses para pagar: "))

parcela = valorEmprestimo / quantMeses

salarioDisponivel = salario * 0.3

os.system('cls')
sys.stdout.write("\nCalculando aprovação de empréstimo...\n")
time.sleep(3)
os.system('cls')

if (parcela >= salarioDisponivel):
    print("\nEmpréstimo não aprovado.\n")
    print("O valor da parcela (R$ {:.2f}) é maior ou igual a 30% do seu salario (R$ {:.2f}).\n".format(parcela, salarioDisponivel))
else:
    print("\nEmpréstimo aprovado!\n")
    print("O valor da parcela (R$ {:.2f}) é menor que 30% do seu salario (R$ {:.2f}).\n".format(parcela, salarioDisponivel))