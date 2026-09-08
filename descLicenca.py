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

quantLicencas = int(input("Informe quantas licenças você quer comprar: "))

total = quantLicencas * 150

os.system('cls')
sys.stdout.write("\nCalculando valor total...\n")
time.sleep(3)
os.system('cls')

print("\nO valor total de licenças é R$ {:.2f}\n".format(total))

if (quantLicencas >= 50):
    total -= 500
    print("Mas você recebeu o desconto!!! O valor total da compra fica R${:.2f}\n".format(total)) 