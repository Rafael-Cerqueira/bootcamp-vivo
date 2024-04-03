import textwrap


def menu():

    menu_texto = """\n
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair
    => """

    return input(textwrap.dedent(menu_texto))


def depositar(saldo, valor, extrato, /):

    if valor > 0:

        saldo += valor
        extrato += f'==== Depósito: R$ {valor:.2f} ====\n'

    else:
        print("#### Valor precisa ser maior que 0! ####")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("#### Valor precisa ser menor que o saldo! ####")
    elif valor > limite:
        print("#### Você excedeu o limite de valor por saque! ####")
    elif numero_saques >= limite_saques:
        print("#### Você excedeu o limite de saque diário! ####")

    else:
        saldo -= valor
        extrato += f'==== Saque: R$ {valor:.2f} ====\n'
        numero_saques += 1

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    if not extrato:
        print("#### Não houveram movimentações ####")
    else:
        extrato
        print(f"==== Saldo: R$ {saldo:.2f} ====")


def criar_usuario(usuarios):

    cpf = input('Digite o numero do seu CPF: ')
    nome = input('Digite o seu nome: ')
    data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Digite o nome da Rua: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("#### Já existe um usuário com esse mesmo cpf! ###")
    else:
        usuarios.append({"nome": nome, "Data de nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco,})
        print("==== Usuário criado com sucesso! ====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    if not usuarios_filtrados:
        return None
    else:
        return usuarios_filtrados[0]

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o numero do seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}       
    else:
        print("#### Usuario não encontrado ###")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")        

if __name__ == "__main__":
    main()
