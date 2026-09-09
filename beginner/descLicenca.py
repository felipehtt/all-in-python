import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de desconto de licenças.\n")

print("Cada licença custa R$ 150,00. Comprando mais de 50 licenças, você recebe um desconto de R$ 500,00 no valor total.\n")
time.sleep(2)

quant_licencas = int(input("Informe quantas licenças você quer comprar: "))

total = quant_licencas * 150

os.system('cls')
sys.stdout.write("\nCalculando valor total...\n")
time.sleep(3)
os.system('cls')

print(f"\nO valor total de licenças é R$ {total:.2f}\n")

if (quant_licencas > 50):
    total -= 500
    print(f"Mas você recebeu o desconto!!! O valor total da compra fica R$ {total:.2f}\n") 