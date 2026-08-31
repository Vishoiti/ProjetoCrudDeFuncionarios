import os
os.system("cls")

from subalgoritmo import exibir_menu

crud = {}


while True:

    exibir_menu()
    escolha = input("Digite um número: ")

    match escolha:
        case "0":
            print("O Programa terminou!")
            break

