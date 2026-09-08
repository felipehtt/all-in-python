import os
import sys
import time

os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de verificação de temperatura.\n")
temp = float(input("Informe a temperatura do servidor: "))

os.system('cls')
sys.stdout.write("\nVerificando temperatura...\n")
time.sleep(3)
os.system('cls')

if temp > 75:
    print(f"\nALERTA: Ligar refrigeração extra! Temperatura: {temp:.1f}°C\n")
else:
    print(f"\nTemperatura dentro do padrão. Temperatura: {temp:.1f}°C\n")