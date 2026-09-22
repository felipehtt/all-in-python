import os, sys, time

def validar_login(user, senha):
    if user == "admin" and senha == "sys123":
        print("\nAcesso permitido.\n")
    else:
        print("\nAcesso negado.\n")


os.system('cls')
sys.stdout.write("\nCarregando programa...\n")
time.sleep(2)
os.system('cls')

print("\nPrograma de validação de login.\n")
user = input("Informe o usuário: ")
senha = input("Informe a senha: ")

os.system('cls')
sys.stdout.write("\nValidando login...\n")
time.sleep(3)
os.system('cls')

validar_login(user, senha)