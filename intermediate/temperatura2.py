import os, sys, time

def monitorar_temperatura(temperatura):
    if temperatura > 75:
        print(f"\nALERTA: Ligar refrigeração extra! Temperatura: {temperatura:.1f}°C\n")
    else:
        print(f"\nTemperatura dentro do padrão. Temperatura: {temperatura:.1f}°C\n")

try:

    os.system('cls')
    sys.stdout.write("\nCarregando programa...\n")
    time.sleep(2)
    os.system('cls')

    print("\nPrograma de verificação de temperatura.\n")
    temperatura = float(input("Informe a temperatura do servidor: "))

    os.system('cls')
    sys.stdout.write("\nVerificando temperatura...\n")
    time.sleep(3)
    os.system('cls')

    monitorar_temperatura(temperatura)

except ValueError:
    print("\nErro: Por favor, insira apenas números válidos.\n")