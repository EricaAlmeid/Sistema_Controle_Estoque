# Sistema de Controle de Estoque para Loja de Eletrônicos em Python 📦💻

Este repositório contém a primeira etapa do desenvolvimento de um sistema simples de controle de estoque, construído em **Python**. O projeto foi criado como um estudo de caso para aplicar e solidificar conceitos fundamentais de lógica computacional, controle de fluxo e estruturas de dados.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é desenvolver uma base funcional para um sistema de controle de estoque, que permita gerenciar produtos em uma loja de eletrônicos. Focamos em implementar as operações CRUD (Create, Read, Update, Delete) básicas, utilizando apenas os recursos nativos do Python para simular o gerenciamento de dados.

---

## ✨ Funcionalidades Implementadas

O sistema oferece as seguintes funcionalidades, acessíveis através de um menu interativo:

1.  **Adicionar Produto:**
    * Permite cadastrar novos produtos no estoque.
    * Solicita o **nome**, **preço** e **quantidade em estoque**.
    * Inclui **validação** para garantir que o nome do produto seja **único** e que preço e quantidade sejam valores válidos (numéricos e positivos).
2.  **Atualizar Produto:**
    * Permite modificar o **preço** e a **quantidade em estoque** de um produto já existente.
    * O produto é identificado pelo seu **nome**.
3.  **Excluir Produto:**
    * Permite remover um produto do estoque.
    * O produto é identificado pelo seu **nome**.
4.  **Visualizar Estoque:**
    * Exibe uma lista organizada de todos os produtos atualmente no estoque.
    * Para cada produto, são mostrados o **nome**, **preço** e **quantidade em estoque**.
5.  **Sair do Sistema:**
    * Encerra a execução do programa.

---

## 🚀 Como Executar o Sistema

Para rodar este sistema em sua máquina, siga os passos abaixo:

1.  **Clone o repositório** (ou copie o código Python para um arquivo `.py`):
    ```bash
    git clone <link_do_seu_repositorio>
    cd <nome_do_seu_repositorio>
    ```
    (Substitua `<link_do_seu_repositorio>` e `<nome_do_seu_repositorio>` pelo URL e nome do seu repositório no GitHub.)

2.  **Certifique-se de ter Python instalado.** Este projeto foi desenvolvido com Python 3.x.

3.  **Execute o arquivo Python** a partir do seu terminal:
    ```bash
    python nome_do_seu_arquivo.py
    ```
    (Se você salvou o código como `sistema_estoque.py`, o comando seria `python sistema_estoque.py`)

4.  Siga as instruções do menu que aparecerá no terminal para interagir com o sistema.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: A linguagem de programação utilizada para construir a lógica do sistema.
* **Estruturas de Dados**: Listas (`list`) e Dicionários (`dict`) do Python para armazenar e organizar os dados dos produtos.
* **Controle de Fluxo**: Estruturas `if`, `elif`, `else` e laços `for`, `while` para gerenciar a navegação do menu, validação de entrada e manipulação dos dados.

---

## 🧠 Conceitos Aplicados

Este projeto é uma demonstração prática de:

* **Lógica Computacional**: Resolução de problemas através de algoritmos claros e sequenciais.
* **Controle de Fluxo**: Utilização de condicionais e loops para direcionar a execução do programa com base nas interações do usuário e nos dados.
* **Estruturas de Dados**: A escolha e aplicação de listas de dicionários para representar e organizar informações complexas (cada produto como um dicionário com seus atributos, armazenados em uma lista).
* **Modularização**: Organização do código em funções (`adicionar_produto`, `atualizar_produto`, etc.) para melhorar a legibilidade e manutenção.
* **Tratamento de Erros**: Uso de blocos `try-except` para lidar com entradas inválidas do usuário, tornando o sistema mais robusto.
* **Boas Práticas de Programação**: Código com comentários explicativos, nomes de variáveis claros e uma estrutura organizada.

---

## Próximos Passos (Possíveis Evoluções)

Para futuras expansões, o sistema poderia incluir:

* **Persistência de Dados**: Salvar e carregar o estoque em um arquivo (CSV, JSON) ou banco de dados para que os dados não sejam perdidos ao fechar o programa.
* **Pesquisa Avançada**: Funcionalidades de busca por diferentes critérios (por preço, quantidade, parte do nome).
* **Controle de Vendas**: Adicionar um módulo para registrar vendas e atualizar automaticamente a quantidade em estoque.
* **Refatoração da Estrutura de Dados**: Para estoques muito grandes, considerar um dicionário onde a chave é o código do produto para buscas mais rápidas (em vez de uma lista).
* **Interface Gráfica (GUI)**: Utilizar bibliotecas como Tkinter, PyQt ou Kivy para criar uma interface mais amigável que não seja apenas no terminal.

---

## Contribuição

Sinta-se à vontade para explorar o código, sugerir melhorias ou reportar problemas!

---

## Licença

Este projeto está sob a licença [MIT License](LICENSE).
