from cliente import Cliente

class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, cpf, email, endereco, telefone):
        try:
            cliente = Cliente(nome, cpf, email, endereco, telefone)
            self.clientes.append(cliente)
            cliente.gerar_pdf_cadastro()
        except ValueError as e:
            print(e)

    def excluir_cliente(self, cpf, motivo):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                cliente.gerar_pdf_exclusao(motivo)
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nome} excluído com sucesso!")
                return
        print(f"Cliente com CPF {cpf} não encontrado.")
