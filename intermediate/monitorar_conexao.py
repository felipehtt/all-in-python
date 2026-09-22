import os, time

def monitorar_servico():
    status = "n"

    while status == "n":
        os.system('cls')
        print("\nAguardando conexão...\n")
        time.sleep(3)
        validar = input("O serviço voltou a responder? (s/n): ")

        if validar == "s":
            os.system('cls')
            print("\nServiço restaurado com sucesso!\n")
            break
        else:
            if validar != "n":
                print("\nComando inválido! Por favor, digite apenas 's' ou 'n'.\n")
                time.sleep(2)
                status = "n"
            else:
                status = validar

monitorar_servico()