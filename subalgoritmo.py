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
        return
    
    nome = str(input("Nome......: "))
    salario = float(input("Salário.: "))

    funcionario = {
        "cpf": cpf,
        "nome": nome,
        "salario": salario
    }
    
    c[cpf] = funcionario

    print("""
        =========================   
        CADASTRADO COM SUCESSO!
        ========================= 
        """)

def consultar_funcionario(c: dict) -> None:
    print("""
    CONSULTANDO FUNCIONÁRIO 
    =========================   
    """)
    cpf = int(input("CPF.....: "))

    if cpf in c:
        funcionario = c[cpf]

        print("""
        =====================""")
        print(f"CPF.....: {funcionario['cpf']}")
        print(f"Nome....: {funcionario['nome']}")
        print(f"Salário.: {funcionario['salario']}")
        print("""
            =====================""")
    else:
        print("""
            ==========================
             Funcionário inexistente!
            ==========================
        """)