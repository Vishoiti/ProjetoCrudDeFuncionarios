def exibir_menu() -> None:
    print("""
            M E N U
            ===========================
            0 - SAIR
            1 - Cadastrar Funcionário
            2 - Consultar Funcionário
            3 - Editar Funcionário
            4 - Excluir Funcionário
            5 - Listar funcionários
    """)

def inserir_dados(c: dict) -> None:
    cpf = int(input("CPF......: "))
    if cpf in c:
        print("""
             ==========================   
               FUNCIONÁRIO JÁ EXISTE!
             ==========================
        """)
    else:
        nome = str(input("Nome......: "))
        salario = float(input("Salário.: "))

    print("""
       =========================   
        CADASTRADO COM SUCESSO!
       ========================= 
        """)

    funcionario = {
        "CPF......:" : cpf,
        "Nome......:" : nome,
        "Salário.:" : salario
    }
    return funcionario


    

