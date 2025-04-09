import textwrap

def menu():
    menu = """\n
    =============== MENU ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tInvestir
    [5]\tSaque investimento
    [6]\tNovo Usuário
    [7]\tNova Conta
    [8]\tListar Contas
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, saldo_investimento):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, saldo_investimento, /, *, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f"\nSaldo investido:\t\tR$ {saldo_investimento:.2f}")
    print("=====================================")

def investir(saldo, valor, extrato, saldo_investimento, /):
    
    if valor > saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente para investir. @@@")
    
    elif valor > 0:
        saldo -= valor
        saldo_investimento += valor
        extrato += f"Investido:\tR$ {valor:.2f}\n"
        print("\n=== Dinheiro investido com sucesso! ===")
    
    else:
        print("\n@@@ Operação falhou! Valor informado é inválido. @@@")

    return saldo, extrato, saldo_investimento

def saque_investimento(saldo, valor, extrato, saldo_investimento):
    saldo_investimento_insuficiente = valor > saldo_investimento

    if saldo_investimento_insuficiente:
        print("Operação falhou! Seu saldo investido não é suficiente.")

    elif valor > 0:
        saldo_investimento -= valor
        saldo += valor
        extrato += f"Saque do investimento: R$ {valor:.2f}\n"
        print("\n=== Saque do investimento realizado com sucesso! ===")

    else:
        print("Valor inválido para saque de investimento.")

    return saldo, extrato, saldo_investimento

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ usuario não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    saldo_investimento = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
        
    while True:
        
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )        
        
        elif opcao == "3":
            exibir_extrato(saldo, saldo_investimento, extrato=extrato)

        elif opcao == "4":
            valor = float(input("Informe o valor para investir: "))
            
            saldo, extrato, saldo_investimento = investir(saldo, valor, extrato, saldo_investimento)
        
        elif opcao == "5":
            valor = float(input("Informe o valor para sacar do investimento: "))

            saldo, extrato, saldo_investimento = saque_investimento(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                saldo_investimento=saldo_investimento,
                )
            
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "8":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione uma das operações do menu")
main()