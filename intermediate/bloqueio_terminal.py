import os

def liberar_terminal():
    tentativas = 0
    print("\nOlá!\n")
    while (tentativas < 3):
        senha = input("Digite a senha para acessar o Terminal: ")
        if senha == "suporte2026":
            os.system('cls')
            print("\nTerminal liberado.\n")
            break
        else:
            os.system('cls')
            tentativas += 1
            restantes = 3 - tentativas
            print(f"\nSenha incorreta. Você ainda tem {restantes} tentativa(s).\n")
    if tentativas == 3 and senha != "suporte2026":
        os.system('cls')
        print("\nSistema bloqueado.\n")


liberar_terminal()