import os
import sys
import time

sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de validação de acesso.\n")

user = input("Informe o nome de usuário: ")
password = input("Informe a senha: ")

os.system('cls')
sys.stdout.write("\nValidando acesso...\n")
time.sleep(3)
os.system('cls')

if (user == "admin" and password == "sys123"):
    print("\nAcesso permitido.\n")
else:
    print("\nAcesso negado.\n")