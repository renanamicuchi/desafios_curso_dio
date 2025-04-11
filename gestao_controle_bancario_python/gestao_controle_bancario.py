def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TODO: Adicione o valor da transação ao saldo
        saldo += transacao

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f"Saldo: R$ {saldo:.2f}"

# Lê a entrada do usuário
entrada_usuario = input("Informe o valor para deposito ou saque: ")

# Processa a entrada removendo colchetes e espaços
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

# Converte a string de entrada em uma lista de floats
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Imprime o resultado
print(resultado)