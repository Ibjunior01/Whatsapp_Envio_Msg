# Service serve para a interface não acessar o banco diretamente.

from models.contato import Contato
from repositories.contato_repository import ContatoRepository


class ContatoService:

    def __init__(self):
        self.repository = ContatoRepository()

    def criar_contato(
        self,
        nome,
        telefone,
        empresa="",
        observacoes=""
    ):

        contato = Contato(
            nome=nome,
            telefone=telefone,
            empresa=empresa,
            observacoes=observacoes
        )

        self.repository.criar(contato)

    def listar_contatos(self):
        return self.repository.listar()