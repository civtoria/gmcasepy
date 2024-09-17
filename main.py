from sistema_cadastro import SistemaCadastro

def main():
    sistema = SistemaCadastro()

    # Cadastrando clientes
    sistema.cadastrar_cliente("Victoria", "123.456.789-09", "victoria@email.com", "Rua 1, Bairro 2", "99999-9999")
    sistema.cadastrar_cliente("Layla", "987.654.321-00", "layla@email.com", "Rua 3, Bairro 4", "88888-8888")

    # Excluindo cliente
    sistema.excluir_cliente("123.456.789-09", "Solicitação do cliente")

if __name__ == "__main__":
    main()