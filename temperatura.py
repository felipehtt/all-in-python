import os
import sys
import time

sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de verificação de temperatura.\n")
temp = float(input("Informe a temperatura do servidor: "))

os.system('cls')
sys.stdout.write("\nVerificando temperatura...\n")
time.sleep(2)
os.system('cls')

if temp >= 78.5:
    print("\nALERTA: Ligar refrigeração extra!\n")
else:
    print("\nTemperatura dentro do padrão.\n")