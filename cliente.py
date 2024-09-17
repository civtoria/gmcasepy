import re
import os
from datetime import datetime
from fpdf import FPDF

class Cliente:
    def __init__(self, nome, cpf, email, endereco, telefone):
        self.nome = nome
        if self.validar_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido")
        if self.validar_email(email):
            self.email = email
        else:
            raise ValueError("Email inválido")
        self.endereco = endereco
        self.telefone = telefone

    @staticmethod
    def validar_cpf(cpf):
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        def calc_digito(cpf, multiplicadores):
            soma = sum([int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores))])
            resto = (soma * 10) % 11
            return resto if resto < 10 else 0
        if calc_digito(cpf[:9], range(10, 1, -1)) == int(cpf[9]) and calc_digito(cpf[:10], range(11, 1, -1)) == int(cpf[10]):
            return True
        return False

    @staticmethod
    def validar_email(email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao, email) is not None

    def gerar_pdf_cadastro(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        pdf.cell(200, 10, txt="Cadastro de Cliente", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Nome: {self.nome}", ln=True)
        pdf.cell(200, 10, txt=f"CPF: {self.cpf}", ln=True)
        pdf.cell(200, 10, txt=f"Data de Emissão: {data}", ln=True)
        
        # Diretório com os logs de cadastro
        diretorio = "logs/cadastro/"
        
        # Verifica se o diretório existe, caso contrário cria
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Salva o arquivo PDF
        arquivo = os.path.join(diretorio, f"cadastro_{self.cpf}.pdf")
        pdf.output(arquivo)
        print(f"Arquivo PDF '{arquivo}' gerado com sucesso!")

    def gerar_pdf_exclusao(self, motivo):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        pdf.cell(200, 10, txt="Exclusão de Cliente", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Nome: {self.nome}", ln=True)
        pdf.cell(200, 10, txt=f"CPF: {self.cpf}", ln=True)
        pdf.cell(200, 10, txt=f"Data de Cancelamento: {data}", ln=True)
        pdf.cell(200, 10, txt=f"Motivo: {motivo}", ln=True)

        # Diretório com os logs de exclusão
        diretorio = "logs/exclusao/"
        
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        arquivo = os.path.join(diretorio, f"exclusao_{self.cpf}.pdf")
        pdf.output(arquivo)
        print(f"Arquivo PDF '{arquivo}' gerado com sucesso!")
