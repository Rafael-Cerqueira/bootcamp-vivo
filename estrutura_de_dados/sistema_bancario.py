menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair
===> 
"""

LIMITE = 500
saldo = 0
quantidade_saque = 0
lista_extrato = []

while True:

    resposta = input(menu)

    if resposta == "s":
        valor = float(input("Digite o valor do saque: \n"))
        excede_limite = valor > LIMITE
        excede_saque = quantidade_saque > 3
        excede_saldo = valor > saldo

        if excede_limite:
            print("Valor precisa ser menor que R$ 500.00!")
        elif excede_saque:
            print("Número de saques excedido!")
        elif excede_saldo:
            print("Valor precisa ser menor que o saldo!")
        elif valor > 0:
            saldo -= valor
            quantidade_saque += 1
            saque = f"Saque: R$ {valor:.2f}!"
            lista_extrato.append(saque)
            print(saque)
    
    elif resposta == "d":
        valor = float(input("Digite o valor do deposito: \n"))

        if valor > 0:
            saldo += valor
            deposito = f"Depósito: R$ {valor:.2f}!"
            lista_extrato.append(deposito)
            print(len(lista_extrato))
            print(deposito)

    elif resposta == "e":
        if not len(lista_extrato) > 0:
            print("Não houveram moviemntações na conta!")
        for transacoes in lista_extrato:
            print(transacoes)
        print(f"Saldo total: R$ {saldo:.2f}!")

    elif resposta == "q":
        break