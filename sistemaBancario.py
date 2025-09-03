
def conferir_cadastro(usuarios):
    cpf = input("Informe o CPF do usuário (somentos números):\n ")
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return cpf, usuario[0] if usuario else None


def cadastrar_usuario(usuarios):
    cpf, usuario = conferir_cadastro(usuarios)
    if usuario:
        print("Usuário já cadastrado\n")
        return
    nome = input("Informe o nome para cadastro: ")
    data_nascimento = input("Informe da data de nascimento: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereço": endereco})
    print("Usuário cadastrado!")


def abrir_conta(AGENCIA, numero_conta, usuarios):
    cpf, usuario = conferir_cadastro(usuarios)
    if usuario:
        conta = {'agencia': AGENCIA, 'c/c': numero_conta,
                 'titular': usuario, 'saldo': 0, "extrato": ""}
        print("Conta aberta com sucesso!\n")
        return conta
    print("Usúario não cadastrado! Abertura de conta encerrada.\n ")


def listar_contas(contas):
    for conta in contas:
        print(
            f"Agência: {conta['agencia']}\ncc: {conta['c/c']}\nTitular: {conta['titular']['nome']}\nSaldo: {conta['saldo']}\n")


def depositar(contas, usuarios):
    cpf, usuario = conferir_cadastro(usuarios)
    if not usuario:
        print("Usuário não encontrado")
        return
    cc = int(input("Informe o número da conta corrente"))
    for conta in contas:
        if conta['c/c'] == cc and usuario['nome'] == conta['titular']['nome']:
            deposito = int(input("Informe o valor do deposito: "))
            conta['saldo'] += deposito
            conta['extrato'] += f"Depósito:+R${deposito}\n "
            break

    else:
        print("Conta não encontrada")


def sacar(contas, usuarios):
    cpf, usuario = conferir_cadastro(usuarios)
    if not usuario:
        print("Usuário não encontrado")
        return
    cc = int(input("Informe o número da conta corrente"))

    for conta in contas:
        if conta['c/c'] == cc and usuario['nome'] == conta['titular']['nome']:
            saque = int(input("Informe o valor de saque"))
            while saque > conta['saldo']:
                saque = int(
                    input("Saldo insuficiente, informe novo valor de saque! "))
            conta['saldo'] -= saque
            conta['extrato'] += f"Saque:-R${saque}\n "
            break
    else:
        print("Conta não encontrada")


def exibir_extrato(contas, usuarios):
    cpf, usuario = conferir_cadastro(usuarios)
    if not usuario:
        print("Usuário não encontrado")
        return
    cc = int(input("Informe o número da conta corrente"))
    for conta in contas:
        if conta['c/c'] == cc and usuario['nome'] == conta['titular']['nome']:
            print(f"Extrato: ")
            print(
                f"Agência: {conta['agencia']}\nConta: {conta['c/c']}\nTitular: {conta['titular']['nome']}\n{conta['extrato']}")
            break
    else:
        print("Conta não encontrada")


def main():
    menu = """
        [nu] Novo usuário
        [nc] Nova conta
        [lc] Listar contas
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
"""

    LIMITE_SAQUEs = 3
    AGENCIA = "001"
    contas = []
    usuarios = []
    while True:
        print(menu)
        entrada = input("Escolha a opção desejada: ")

        if entrada == 'nu':
            cadastrar_usuario(usuarios)

        elif entrada == 'nc':
            numero_conta = len(contas) + 1
            conta = abrir_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif entrada == 'lc':
            listar_contas(contas)

        elif entrada == 'd':
            depositar(contas, usuarios)

        elif entrada == 's':
            sacar(contas, usuarios)

        elif entrada == 'e':
            exibir_extrato(contas, usuarios)

        elif entrada == 'q':
            break


if __name__ == '__main__':
    main()
