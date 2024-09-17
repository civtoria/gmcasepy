# Sistema de Cadastro e Exclusão de Clientes

Este projeto é um sistema simples para cadastrar e excluir clientes, gerando arquivos PDF com as informações de cadastro e exclusão. O sistema utiliza a biblioteca `fpdf` para gerar os PDFs e valida os dados do cliente, como CPF e email.

## Estrutura do Projeto

O projeto é composto por três arquivos principais:

1. **`cliente.py`**: Contém a classe `Cliente` responsável por armazenar as informações dos clientes e gerar PDFs para cadastro e exclusão.
2. **`sistema_cadastro.py`**: Contém a classe `SistemaCadastro`, que gerencia a lista de clientes e realiza as operações de cadastro e exclusão.
3. **`main.py`**: Contém o ponto de entrada do programa, onde os clientes são cadastrados e excluídos.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. O projeto utiliza a biblioteca `fpdf`, que pode ser instalada usando pip:

```bash
pip install fpdf
```

## Como Executar

1. **Clone o repositório** (ou baixe os arquivos do projeto):

    ```bash
    git clone https://github.com/civtoria/gmcasepy.git
    ```

2. **Execute o script principal**:

    ```bash
    python main.py
    ```

    Isso irá cadastrar dois clientes e excluir um cliente, gerando os PDFs correspondentes.

## Descrição dos Arquivos

### `cliente.py`

Define a classe `Cliente` com os seguintes métodos e atributos:

- **Método `__init__`**: Inicializa um cliente com nome, CPF, email, endereço e telefone. Valida CPF e email.
- **Método `validar_cpf`**: Valida o CPF fornecido.
- **Método `validar_email`**: Valida o email fornecido.
- **Método `gerar_pdf_cadastro`**: Gera um PDF com as informações de cadastro e salva no diretório `logs/cadastro/`.
- **Método `gerar_pdf_exclusao`**: Gera um PDF com as informações de exclusão e salva no diretório `logs/exclusao/`.

### `sistema_cadastro.py`

Define a classe `SistemaCadastro` com os seguintes métodos:

- **Método `__init__`**: Inicializa uma lista vazia de clientes.
- **Método `cadastrar_cliente`**: Adiciona um novo cliente à lista e gera o PDF de cadastro.
- **Método `excluir_cliente`**: Remove um cliente da lista e gera o PDF de exclusão.

### `main.py`

Ponto de entrada do programa. Cadastra dois clientes e exclui um cliente para demonstrar o funcionamento do sistema.

## Observações

- **Diretórios de PDF**: Certifique-se de que os diretórios `logs/cadastro/` e `logs/exclusao/` existem ou serão criados automaticamente pelo código. Esses diretórios são onde os PDFs serão salvos.
- **Validação de CPF**: A validação de CPF é baseada em regras simples de formatação e cálculo. Certifique-se de usar CPFs válidos.


