# Desafio DIO: Modelando o Sistema Bancário com Programação Orientada a Objetos em Python

Este repositório contém a resolução do desafio de projeto "Modelando o Sistema Bancário com POO em Python", uma evolução do desafio anterior proposto pela Digital Innovation One (DIO)

O objetivo principal foi refatorar o sistema bancário, que antes era estruturado com funções, para uma arquitetura baseada em **Programação Orientada a Objetos (POO)**. Essa nova abordagem visa representar as entidades do mundo real (como Clientes e Contas) de forma mais clara e coesa, melhorando a organização, o encapsulamento e a manutenibilidade do código.

## 🚀 Funcionalidades

O sistema continua a oferecer as operações essenciais de um sistema bancário:

-   **Cadastrar novos usuários (Clientes):** Adiciona novos clientes ao sistema, validando se o CPF já existe.
-   **Criar novas contas correntes:** Vincula uma nova conta a um cliente existente.
-   **Listar contas cadastradas:** Exibe detalhes de todas as contas abertas.
-   **Realizar depósitos:** Adiciona valores ao saldo de uma conta, registrando a transação.
-   **Realizar saques:** Retira valores do saldo, aplicando regras de negócio como limite de saques e valor máximo por transação.
-   **Exibir extrato:** Mostra o histórico detalhado de transações (depósitos e saques) de uma conta.
-   **Sair:** Encerra a execução do programa.

## 🛠️ Tecnologias Utilizadas

-   **Python 3:** O projeto foi desenvolvido inteiramente em Python, utilizando os princípios de POO.

## 🏛️ Arquitetura Orientada a Objetos

O código foi reestruturado em classes para representar os diferentes componentes do sistema bancário, melhorando a coesão e o encapsulamento das responsabilidades:

-   **`Cliente`**: Classe que representa o cliente do banco. Armazena dados pessoais como nome, data de nascimento e CPF, além de um histórico de contas associadas.
-   **`Conta`**: Classe base que abstrai os atributos e métodos comuns a todas as contas, como saldo, agência, número e o histórico de transações.
-   **`ContaCorrente`**: Herda da classe `Conta` e implementa as regras de negócio específicas para contas correntes, como o limite de saques diários e o valor máximo por saque.
-   **`Historico`**: Classe responsável por registrar e gerenciar todas as transações (depósitos e saques) realizadas em uma conta.
-   **`Transacao`** (e suas subclasses `Deposito` e `Saque`): Classes que modelam as operações financeiras, permitindo que cada transação seja registrada como um objeto individual no histórico da conta.

## 💡 Melhorias Futuras

Com a base sólida da POO, o projeto está pronto para novas evoluções:

- [ ] **Persistência de Dados:** Implementar uma forma de salvar e carregar os dados (usando arquivos JSON, Pickle ou um banco de dados) para que as informações não se percam ao fechar o programa.
- [ ] **Tratamento de Erros:** Aprimorar o tratamento de erros para entradas inválidas do usuário (ex: letras em campos numéricos), utilizando blocos `try-except` para uma experiência mais robusta.
- [ ] **Validação de Formato de Dados:** Implementar checagens mais rigorosas para garantir que dados como **CPF** (11 dígitos) e **data de nascimento** sejam inseridos em formatos válidos.

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
 
