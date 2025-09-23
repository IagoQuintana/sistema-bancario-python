# Desafio DIO: Modelando o Sistema Bancário com Programação Orientada a Objetos em Python

Este repositório contém uma versão avançada do desafio de projeto "Modelando o Sistema Bancário com POO", proposto pela Digital Innovation One (DIO). 
O projeto original foi aprimorado com a aplicação de conceitos como **Decorators**, **Iterators** e **Generators**, além de regras de negócio mais complexas.
O objetivo foi transformar um sistema bancário funcional em uma aplicação mais robusta, eficiente e aderente às boas práticas de desenvolvimento Python, aprofundando a estrutura orientada a objetos.


## 🚀 Funcionalidades

O sistema agora conta com funcionalidades mais sofisticadas:

-   **Cadastro de Clientes e Contas:** A base do sistema, permitindo a criação de clientes (Pessoa Física) e a vinculação de contas correntes.
-   **Operações de Saque e Depósito:** Transações financeiras com validações de saldo, valor e limites.
-   **Extrato Detalhado e Filtrável:** Permite visualizar o histórico de transações com a opção de filtrar por **depósitos**, **saques** ou ver **todas as movimentações**. Cada transação agora inclui data e hora.
-   **Limite de Transações Diárias:** O sistema implementa uma regra de negócio que limita o número de transações (saques e depósitos) a **10 por dia** para cada conta.
-   **Listagem de Contas Otimizada:** Utiliza um iterador customizado para percorrer e exibir as contas cadastradas de forma eficiente.
-   **Log de Transações no Console:** Todas as operações principais (saque, depósito, extrato) são registradas no console com data e hora, através de um decorator.

  
## 🛠️ Tecnologias Utilizadas

Para construir esta versão, foram utilizados diversos recursos da linguagem Python:

-   **Python 3**
-   **Programação Orientada a Objetos (POO):** Uso de classes, herança, polimorfismo e encapsulamento para modelar o sistema.
-   **Classes Abstratas (ABC):** Para definir "contratos" e garantir que classes como `Transacao` sejam implementadas corretamente.
-   **Decorators:** O decorator `@log_transacao` foi criado para adicionar a funcionalidade de logging de forma limpa e desacoplada do código principal das funções.
-   **Iterators:** A classe `ContasIterador` implementa o protocolo de iteração para percorrer a lista de contas de maneira "pythônica".
-   **Generators:** O método `gerar_relatorio` na classe `Historico` utiliza `yield` para criar um gerador, otimizando o consumo de memória ao filtrar transações.
-   **Módulo `datetime`:** Para registrar o timestamp preciso de cada transação.


## 🏛️ Arquitetura Orientada a Objetos

O código foi organizado nas seguintes classes principais:

-   **`Cliente`** e **`PessoaFisica`**: Modelam o cliente e seus dados, além de gerenciar a relação com suas contas e aplicar regras de transação.
-   **`Conta`** e **`ContaCorrente`**: Representam as contas bancárias, controlando saldo, limites e o histórico de operações.
-   **`Historico`**: Gerencia a lista de transações de uma conta, permitindo a adição de novas transações, o controle do limite diário e a geração de relatórios filtrados.
-   **`Transacao`**, **`Saque`** e **`Deposito`**: Classes que representam as operações financeiras, registrando seu valor e tipo.


## 💡 Melhorias Futuras

Com a base sólida da POO, o projeto está pronto para novas evoluções:

- [ ] **Persistência de Dados:** Implementar uma forma de salvar e carregar os dados (usando arquivos JSON, Pickle ou um banco de dados) para que as informações não se percam ao fechar o programa.
- [ ] **Tratamento de Erros:** Aprimorar o tratamento de erros para entradas inválidas do usuário (ex: letras em campos numéricos), utilizando blocos `try-except` para uma experiência mais robusta.
- [ ] **Validação de Formato de Dados:** Implementar checagens mais rigorosas para garantir que dados como **CPF** (11 dígitos) e **data de nascimento** sejam inseridos em formatos válidos.
- [ ] **Interface Gráfica (GUI):** Desenvolver uma interface gráfica simples para o sistema.


## ⚙️ Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/IagoQuintana/sistema-bancario-python
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd sistema-bancario-python
    ```

3.  **Execute o script Python:**
    ```bash
    python sistemaBancario.py
    ```
    
4.  **Siga as instruções no terminal** para interagir com o sistema bancário.
 
