from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Definição das classes


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_dia()) >= 10:
            print("@@@ Limite diário de transações atingido! @@@ ")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.cpf}>"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def _definir_saldo_inicial(self, valor):
        self._saldo = valor
        return self._saldo

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(
                "\n@@@ Saldo insuficiente para realizar a transação. Operação falhou! @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Valor informado é inválido. Operação falhou! @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Valor informado é inválido. Operação falhou! @@@")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):

        excedeu_limite = valor > self.limite

        if excedeu_limite:
            print(
                "\n@@@ Valor do saque excede o limite de R$ 500,00. Operação falhou! @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

    def __repr__(self):
        return f"<{self.__class__.__name__}: ({self.agencia}, {self.numero}, {self.cliente.nome})>"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_dia(self):
        data_hoje = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_hoje == data_transacao:
                transacoes.append(transacao)

        return transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._indice]
            return f"""
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}"""
        except IndexError:
            raise StopIteration

        finally:
            self._indice += 1


# Implementação do "sistema" menu e operações


def exibir_menu():
    menu = """
    ================ MENU ================
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\t\tSair
    => """
    return input(menu)


def log_trasacao(funcao):
    def wrapper(*args, **kwargs):

        print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        print(funcao.__name__.upper())
        result = funcao(*args, **kwargs)
        with open(ROOT_PATH/"log.txt", "a", encoding="utf-8", newline="") as log:
            log.write(
                f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} Função: '{funcao.__name__}' executada com argumentos {args} e {kwargs}. Retornou {result}\n")

        return result
    return wrapper


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [
        cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]


@log_trasacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)


@log_trasacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)


@log_trasacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    tipo = input(
        "Informe o tipo de transão que deseja visualizar:\n Saques - s\n Depósitos - d\n Todas - t\n")
    if tipo == 't':
        tipo_transacao = None
    elif tipo == 's':
        tipo_transacao = 'saque'
    elif tipo == 'd':
        tipo_transacao = 'deposito'
    if conta:
        print("\n================ EXTRATO ================")
        extrato = ''
        tem_transacao = False

        for transacao in conta.historico.gerar_relatorio(tipo_transacao):
            tem_transacao = True
            extrato += f"\n{transacao['tipo']}:\n{transacao["data"]}\tR$ {transacao['valor']:.2f}"
        if not tem_transacao:
            extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_trasacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_trasacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    print("\n================ LISTA DE CONTAS ================")
    for conta in ContasIterador(contas):
        print(conta)
        print("-" * 30)


def salvar_clientes(clientes):
    try:
        with open(ROOT_PATH/"clientes.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["cpf", "nome", "data_nascimento", "endereco"])
            for cliente in clientes:
                writer.writerow([cliente.cpf, cliente.nome,
                                cliente.data_nascimento, cliente.endereco])
    except IOError as exc:
        print(f"Erro: {exc}")


def salvar_contas(contas):
    try:
        with open(ROOT_PATH/"contas.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["numero", "agencia", "saldo", "limite", "cpf_cliente"])
            for conta in contas:
                writer.writerow([conta.numero, conta.agencia,
                                conta.saldo, conta.limite, conta.cliente.cpf])

    except IOError as exc:
        print(f"Erro: {exc}")


def carregar_clientes():
    clientes_carregados = []
    try:
        with open(ROOT_PATH/"clientes.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                nome = row["nome"]
                cpf = row["cpf"]
                data_nascimento = row["data_nascimento"]
                endereco = row["endereco"]
                novo_cliente = PessoaFisica(
                    nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
                clientes_carregados.append(novo_cliente)

    except IOError as exc:
        print(f"Erro: {exc}")
    return clientes_carregados


def carregar_contas(clientes):
    contas_carregadas = []
    try:
        with open(ROOT_PATH/"contas.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                numero = row["numero"]
                saldo = float(row["saldo"])
                cpf = row["cpf_cliente"]
                cliente = filtrar_cliente(cpf, clientes)
                conta = ContaCorrente.nova_conta(
                    cliente=cliente, numero=numero)
                conta._definir_saldo_inicial(saldo)
                contas_carregadas.append(conta)
                cliente.adicionar_conta(conta)

    except IOError as exc:
        print(f"Erro: {exc}")

    return contas_carregadas


def main():
    clientes = carregar_clientes()
    contas = carregar_contas(clientes)

    numero_proxima_conta = 1
    if contas:
        numero_proxima_conta = max(int(c.numero) for c in contas) + 1

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_conta(numero_proxima_conta, clientes, contas)
            numero_proxima_conta += 1
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nObrigado por usar nosso sistema! Saindo...")
            salvar_clientes(clientes)
            salvar_contas(contas)
            break
        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
