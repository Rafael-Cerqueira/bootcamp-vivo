def menu():
    opcoes =  """
    [nu] = Novo usuário
    [nc] = Nova Conta
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [lc] = Listar Contas
    [q] = Sair
    ===> 
    """   
    return input(opcoes)


def sacar(*,saldo, valor, extrato, limite, limite_saque, numeros_saque):
    excede_limite = valor > limite
    excede_saque = numeros_saque > limite_saque
    excede_valor = valor > saldo

    if excede_limite:
        print("Valor precisa ser menor de R$ 500.00!")
    elif excede_saque:
        print("Número de saques excedido: 3!")
    elif excede_valor:
        print(f"O valor precisa ser menor que seu saldo! Saldo atual: {saldo:.2f}.")
    elif valor > 0:
        saldo -= valor
        numeros_saque += 1
        saque = f"Saque: {valor:.2f}!"
        extrato.append(saque)
        print(saque)
    else:
        print("Naõ foi possível realizar a operação!")
        
    return saldo, extrato, numeros_saque

def despositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        deposito = f"Depósito: R${valor:.2f}!"
        extrato.append(deposito)
        print(deposito)
    else:
        print("Não foi possível realizar o saque!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if not len(extrato) > 0:
        print("Ainda não houveram movimentações na conta!")
    else:
        for item in extrato:
            print(item)
        print(f"Saldo atual: R$ {saldo:.2f}")

def fitrar_usuarios(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    if usuarios_filtrados:
        return usuarios_filtrados[0]

def criar_usuario(usuarios):
    nome = input("Digite o seu nome completo: ")
    cpf = input("Digite o seu CPF: ")
    endereco = input("Digite o seu endereço. ex. logradouro - nro -  bairro - cidade/sigla: ")

    usuario = {"Nome": nome, "CPF": cpf, "Endereço": endereco}
    usuarios_existentes = fitrar_usuarios(usuarios, cpf)
    if not usuarios_existentes:
        print(f"Usuário {nome} cadastrado!")
    else:
        print(f"Já existe um usuário com esse CPF: {cpf}")
        return None
    return usuario

def criar_conta(usuarios, agencia, conta_corrente):
    cpf = input("Digite o número do seu CPF: ")    
    usuarios_existentes = fitrar_usuarios(usuarios, cpf)
    if usuarios_existentes:
        conta = {"Usuário": usuarios_existentes["Nome"], "Agencia": agencia, "CC": conta_corrente}
        print(f"Conta {conta_corrente} criada em nome de {usuarios_existentes["Nome"]}!")
        return conta
    else:
        print("Usuário não encontrado!")
        return None
    
def listar_contas(lista_contas):
    for conta in lista_contas:
        print(conta)

def main():

    LIMITE = 500
    LIMITE_SAQUE = 3
    saldo = 0
    extrato = []
    numeros_saque = 0
    usuarios = []
    lista_contas = []
    agencia = "0001"

    while True:

        opcao_selecionada = menu()

        if opcao_selecionada == "s":
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato, numeros_saque = sacar(
                                                saldo=saldo, 
                                                valor=valor, 
                                                extrato=extrato, 
                                                limite=LIMITE, 
                                                limite_saque=LIMITE_SAQUE, 
                                                numeros_saque=numeros_saque
                                                )

        elif opcao_selecionada == "d":
            valor = float(input("Digite o valor do deposito: "))

            saldo, extrato = despositar(saldo, valor, extrato)

        elif opcao_selecionada == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao_selecionada == "nu":
            usuario = criar_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)

        elif opcao_selecionada == "nc":
            conta_corrente = len(lista_contas) + 1

            conta = criar_conta(usuarios, agencia, conta_corrente)
            if conta:
                lista_contas.append(conta)

        elif opcao_selecionada == "lc":
            listar_contas(lista_contas)
            
        elif opcao_selecionada == "q":
            break

        else:
            print("** Operação não é valida! **")

if __name__ == "__main__":
    main()