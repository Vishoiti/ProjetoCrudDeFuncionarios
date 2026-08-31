import os
os.system("cls")

from subalgoritmo import exibir_menu, inserir_dados

crud = {}


while True:

    exibir_menu()
    escolha = input("Digite um número: ")

    match escolha:
        case "0":
            print("O Programa terminou!")
            break
        case "1":
            inserir_dados(crud)