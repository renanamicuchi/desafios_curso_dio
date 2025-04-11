def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite:
            # TODO: Adicione a transação à lista filtrada:
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


# Lê a entrada do usuário
entrada = input()

# Divide a entrada em transações e limite
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())  # Converte o limite para float

# Converte a string de transações em uma lista de inteiros
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite
resultado = filtrar_transacoes(transacoes, limite)

# Imprime o resultado no formato solicitado
print(f"Transações: {resultado}")