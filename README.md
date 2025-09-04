# Desafio DIO: Otimizando o Sistema Bancário com Funções Python

Este repositório contém a resolução do desafio de projeto "Otimizando o Sistema Bancário com Funções Python", proposto pela Digital Innovation One (DIO) no bootcamp **Suzano - Python Developer #2**.

O objetivo principal foi refatorar o código do sistema bancário, dividindo-o em funções reutilizáveis para as operações. Essa otimização visa aprimorar a estrutura, a legibilidade e a eficiência do sistema, facilitando sua manutenção e entendimento.

## 🚀 Funcionalidades

O sistema permite realizar as seguintes operações:

-   **Cadastrar novos usuários:** Adiciona novos clientes ao sistema, validando se o CPF já existe.
-   **Abrir novas contas correntes:** Cria uma nova conta e a vincula a um usuário existente.
-   **Listar contas cadastradas:** Exibe detalhes de todas as contas abertas.
-   **Realizar depósitos:** Adiciona um valor ao saldo de uma conta específica.
-   **Realizar saques:** Retira um valor do saldo da conta, com validação de saldo insuficiente.
-   **Exibir extrato:** Mostra o histórico de transações (depósitos e saques) de uma conta.
-   **Sair:** Encerra a execução do programa.

## 🛠️ Tecnologias Utilizadas

-   **Python 3:** O projeto foi desenvolvido inteiramente em Python, sem a necessidade de bibliotecas externas.

## 🔧 Estrutura do Código

O código foi modularizado nas seguintes funções para melhorar a organização e o reuso:

-   `main()`: Função principal que gerencia o menu e o loop de execução do programa.
-   `conferir_cadastro(usuarios)`: Verifica se um usuário já existe com base no CPF.
-   `cadastrar_usuario(usuarios)`: Responsável por cadastrar um novo usuário no sistema.
-   `abrir_conta(AGENCIA, numero_conta, usuarios)`: Cria uma nova conta corrente vinculada a um usuário.
-   `listar_contas(contas)`: Exibe os detalhes de todas as contas cadastradas.
-   `depositar(contas, usuarios)`: Gerencia a lógica para adicionar um valor ao saldo da conta.
-   `sacar(contas, usuarios)`: Gerencia a lógica para retirar um valor do saldo da conta.
-   `exibir_extrato(contas, usuarios)`: Mostra o histórico de transações da conta.

## 💡 Melhorias Futuras

Este projeto é um ponto de partida. Abaixo estão algumas ideias e melhorias que podem ser implementadas no futuro para torná-lo mais robusto e completo:

- [ ] **Programação Orientada a Objetos (POO):** Refatorar o código para utilizar classes (ex: `Cliente`, `Conta`, `Transacao`) para melhor organizar a estrutura e o comportamento do sistema.
- [ ] **Persistência de Dados:** Implementar uma forma de salvar e carregar os dados dos usuários e contas, para que não sejam perdidos ao fechar o programa (usando arquivos JSON ou um banco de dados).
- [ ] **Regras de Negócio para Saque:** Implementar as regras de negócio que faltam na função `sacar`, como o **limite de 3 saques por sessão** e um valor máximo por transação.
- [ ] **Validação de Valores de Transação:** Impedir depósitos e saques de valores **negativos ou nulos**, garantindo a integridade dos dados.
- [ ] **Tratamento de Erros de Entrada:** Adicionar blocos `try-except` para lidar com **entradas não numéricas** em campos de valor, CPF e número da conta, evitando que o programa encerre inesperadamente.
- [ ] **Validação de Formato de Dados:** Implementar checagens para garantir que dados como **CPF** (11 dígitos) e **data de nascimento** sejam inseridos em formatos válidos.
- [ ] **Função de Histórico:** Criar uma classe ou estrutura de dados dedicada para registrar e exibir o histórico de transações de forma mais organizada.
- [ ] **Interface Gráfica (GUI):** Desenvolver uma interface gráfica para uma experiência de usuário mais amigável.

 
## ⚙️ Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/IagoQuintana/Criando-um-Sistema-Banc-rio-com-Python.git](https://github.com/IagoQuintana/Criando-um-Sistema-Banc-rio-com-Python.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Criando-um-Sistema-Banc-rio-com-Python
    ```

3.  **Execute o script Python:**
    ```bash
    python sistemaBancario.py
    ```
    
4.  **Siga as instruções no terminal** para interagir com o sistema bancário.
 

## 📄 Código Fonte

<details>
<summary>Clique para ver o código completo</summary>

```python
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
