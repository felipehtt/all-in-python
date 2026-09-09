import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de previsão de conta de água\n")

junho = float(input("Informe o valor da conta de água do mês de junho: ").replace(",", "."))
julho = float(input("Informe o valor da conta de água do mês de julho: ").replace(",", "."))
agosto = float(input("Informe o valor da conta de água do mês de agosto: ").replace(",", "."))

preco_antigo = 2.50
preco_novo = 3.50

consumo_junho = junho / preco_antigo
consumo_julho = julho / preco_antigo
consumo_agosto = agosto / preco_antigo

media_consumo = (consumo_junho + consumo_julho + consumo_agosto) / 3

previsao_setembro = media_consumo * preco_novo

os.system('cls')
sys.stdout.write("\nCalculando previsão de conta de água...\n")
time.sleep(3)
os.system('cls')

print(f"\nA previsão da conta de água para o mês de setembro é: R$ {previsao_setembro:.2f}\n")