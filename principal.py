import os
os.system("cls")

from subalgoritmo import exibir_menu, inserir_dados, consultar_funcionario, editar_funcionario, excluir_funcionario, listar_funcionario

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
        case "2":
            consultar_funcionario(crud)
        case "3":
            editar_funcionario(crud)
        case "4":
            excluir_funcionario(crud)
        case "5":
            listar_funcionario(crud)