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


def exibir_dados(c:dict) -> None:
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
        return funcionario
    
    else:
        print("""
            ==========================
             Funcionário inexistente!
            ==========================
            """)
        return None

def consultar_funcionario(c: dict) -> None:
    print("""
    CONSULTANDO FUNCIONÁRIO 
    =========================   
    """)
    exibir_dados(c)

def editar_funcionario(c:dict) -> None:
    print("""
        EDITANDO FUNCIONÁRIO 
       ======================   
        """)
    funcionario = exibir_dados(c)
    if funcionario == None:
        return
    
    print("---------------------------")
    print("Edite os campos:")
    print("---------------------------")
    novo_nome = str(input("Nome.....: "))
    novo_salario = float(input("Salário.: "))

    funcionario['nome'] = novo_nome
    funcionario['salario'] = novo_salario

    print("====================")
    print("Editado com sucesso!")
    print("====================")

def excluir_funcionario(c: dict) -> None:
    print("""
        EXCLUINDO FUNCIONÁRIO 
       ======================   
        """)
    funcionario = exibir_dados(c)
    if funcionario == None:
        return

    cpf = funcionario['cpf']

    escolha = input("Confirmar a exclusão do funcionário  [S/N]?: ").lower()
    if escolha == "s":
        del c[cpf]
        print("""
        =====================
        Funcionário excluído!
        =====================
        """)
    else:
        print("Exclusão cancelada . . .")