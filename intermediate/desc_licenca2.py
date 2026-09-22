import os, sys, time

def calcular_licencas(quant_licencas):
    total = quant_licencas * 150
    if quant_licencas > 50:
        total -= 500
    return total

try:

    os.system('cls')
    sys.stdout.write("\nCarregando programa...\n")
    time.sleep(2)
    os.system('cls')

    print("\nPrograma de desconto de licenças.\n")

    print("Cada licença custa R$ 150,00. Comprando mais de 50 licenças, você recebe um desconto de R$ 500,00 no valor total.\n")
    time.sleep(2)

    quant_licencas = int(input("Informe quantas licenças você quer comprar: "))

    total = calcular_licencas(quant_licencas)

    os.system('cls')
    sys.stdout.write("\nCalculando valor total...\n")
    time.sleep(3)
    os.system('cls')

    print(f"\nO valor total de licenças é R$ {total:.2f}\n")

except ValueError:
    print("\nErro: Por favor, insira apenas números válidos.\n")