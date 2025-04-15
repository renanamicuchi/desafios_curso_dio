menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Investir
[5] Saque investimento
[0] Sair

=> """

saldo = 0
saldo_investimento = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor  > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nSaldo investido: R$ {saldo_investimento:.2f}")
        print("=====================================")

    elif opcao == "4":
        valor = float(input("Informe o valor do investimento: "))

        saldo_insuficiente = valor > saldo

        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente para investir.")

        elif valor > 0:
            saldo -= valor
            saldo_investimento += valor
            extrato += f"Investido: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "5":
        valor = float(input("Informe o valor para sacar do investimento: "))

        saldo_investimento_insuficiente = valor > saldo_investimento

        if saldo_investimento_insuficiente:
            print("Operação falhou! Seu saldo investido não é suficiente.")

        elif valor > 0:
            saldo_investimento -= valor
            saldo += valor
            extrato += f"Saque do investimento: R$ {valor:.2f}\n"

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione uma das operações do menu")
    