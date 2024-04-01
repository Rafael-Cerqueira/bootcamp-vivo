menu = """
Digite as opções abaixo para utilizar o sistema bancário:

Opção - Descrição
[d] - Depositar.
[s] - Sacar.
[e] - Extrato
[q] - Sair
\n

"""

saldo = 0
LIMITE_SAQUE = 500
quantidade_saques = 0
lista_extrato = []

def depositar(valor):
    global saldo
    saldo += valor
    deposito = f'Depósito : R$ {valor:.2f}\n'
    lista_extrato.append(deposito)
    return deposito

def sacar(valor):
    global saldo, quantidade_saques

    if quantidade_saques >= 3:
        return 'O Limite é de 3 saques diários.'
    elif valor > LIMITE_SAQUE:
        return 'Valor máximo de saque é R$ 500,00.'
    elif valor > saldo:
        return 'Você não tem saldo suficiente!'
    else:
        saldo -= valor
        saque = f'Saque: R$ {valor:.2f}'
        quantidade_saques += 1
        lista_extrato.append(saque)
        return saque

def extrato():
    for item in lista_extrato:
        print(item)
    print(f'O Seu saldo é: R$ {saldo:.2f}')

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input('\nDigite o valor do deposito: '))
        print(depositar(valor))

    elif opcao == 's':
        valor = float(input('\nDigite o valor do saque: '))
        print(sacar(valor))

    elif opcao == 'e':
        extrato()

    elif opcao == 'q':
        print('Até mais!\n')
        break
