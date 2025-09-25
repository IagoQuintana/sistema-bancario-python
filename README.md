# Desafio DIO: Modelando o Sistema Bancário com POO

Este repositório contém uma versão avançada do desafio de projeto "Modelando o Sistema Bancário com POO", proposto pela Digital Innovation One (DIO). 

O projeto evoluiu para incluir funcionalidades cruciais como **persistência de dados em arquivos CSV** e um **sistema de logging de transações em arquivo de texto**, tornando-o uma aplicação mais completa e robusta.

O objetivo foi solidificar a arquitetura orientada a objetos e adicionar camadas de funcionalidade que garantem que os dados dos usuários não sejam perdidos entre as sessões de uso e que todas as operações sejam auditáveis.


## 🚀 Funcionalidades

O sistema agora oferece um ciclo de vida completo para os dados, além das operações bancárias:

-   **Persistência de Dados (Novo!):** Clientes e contas agora são **salvos automaticamente em arquivos `clientes.csv` e `contas.csv`** ao sair do programa. Ao iniciar, o sistema carrega todos os dados previamente salvos, garantindo a continuidade.
-   **Logging em Arquivo (Aprimorado!):** O decorator `@log_transacao` foi aprimorado para registrar cada operação (depósito, saque, criação de cliente/conta) em um arquivo **`log.txt`**, com data, hora, função executada e argumentos, criando um rastro de auditoria completo.
-   **Extrato Detalhado e Filtrável:** Permite visualizar o histórico de transações com a opção de filtrar por **depósitos**, **saques** ou ver **todas as movimentações**.
-   **Limite de Transações Diárias:** Mantém a regra de negócio que limita o número de transações a **10 por dia** para cada conta.
-   **Listagem de Contas Otimizada:** Utiliza um iterador customizado para percorrer e exibir as contas cadastradas de forma eficiente.

  
## 🛠️ Tecnologias e Conceitos Aplicados

Para construir esta versão, foram utilizados diversos recursos da linguagem Python:

-   **Python 3**
-   **Módulo `csv` (Novo!):** Utilizado para ler e escrever os dados de clientes e contas, implementando a persistência de dados.
-   **Programação Orientada a Objetos (POO):** Estrutura central do projeto, com classes, herança e polimorfismo.
-   **Decorators:** O decorator `@log_trasacao` agora interage com o sistema de arquivos para salvar logs persistentes.
-   **Iterators e Generators:** Utilizados para otimizar a listagem de contas e a geração de relatórios de extrato.
-   **Módulo `datetime`:** Essencial para registrar o timestamp preciso de cada transação no histórico e no arquivo de log.


## 🏛️ Arquitetura Orientada a Objetos

A arquitetura orientada a objetos foi mantida e agora é suportada por um conjunto de funções utilitárias para persistência e logging.

-   **Funções de Persistência (`salvar_clientes`, `carregar_clientes`, `salvar_contas`, `carregar_contas`):** Novas funções responsáveis por serializar os objetos para CSV e desserializá-los ao iniciar o sistema.
-   **`Cliente`** e **`PessoaFisica`**: Modelam o cliente e seus dados, além de gerenciar a relação com suas contas e aplicar regras de transação.
-   **`Conta`** e **`ContaCorrente`**: Representam as contas bancárias, controlando saldo, limites e o histórico de operações.
-   **`Historico`**: Gerencia a lista de transações de uma conta, permitindo a adição de novas transações, o controle do limite diário e a geração de relatórios filtrados.
-   **`Transacao`**, **`Saque`** e **`Deposito`**: Classes que representam as operações financeiras, registrando seu valor e tipo.


## 💡 Melhorias Futuras

Com a base sólida da POO, o projeto está pronto para novas evoluções:

- [ ] **Banco de Dados Relacional:** Substituir a persistência em CSV por um banco de dados mais robusto como **SQLite** para gerenciar relacionamentos e garantir maior integridade dos dados.
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
 
