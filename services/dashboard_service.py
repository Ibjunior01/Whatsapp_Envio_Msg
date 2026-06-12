from repositories.contato_repository import (
    ContatoRepository
)


class DashboardService:

    def __init__(self):

        self.contato_repository = (
            ContatoRepository()
        )

    def total_contatos(self):

        contatos = (
            self.contato_repository.listar()
        )

        return len(contatos)