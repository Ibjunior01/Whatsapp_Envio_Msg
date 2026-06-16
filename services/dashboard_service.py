from repositories.contato_repository import (
    ContatoRepository
)

from repositories.agendamento_repository import (
    AgendamentoRepository
)


class DashboardService:

    def __init__(self):

        self.contato_repository = (
            ContatoRepository()
        )

        self.agendamento_repository = (
            AgendamentoRepository()
        )

    def total_contatos(self):

        contatos = (
            self.contato_repository.listar()
        )

        return len(contatos)

    def total_agendamentos(self):

        agendamentos = (
            self.agendamento_repository.listar()
        )

        return len(agendamentos)

    def total_pendentes(self):

        agendamentos = (
            self.agendamento_repository.listar()
        )

        return len([
            a for a in agendamentos
            if a["status"] == "PENDENTE"
        ])

    def total_enviados(self):

        agendamentos = (
            self.agendamento_repository.listar()
        )

        return len([
            a for a in agendamentos
            if a["status"] == "ENVIADO"
        ])

    def total_falhas(self):

        agendamentos = (
            self.agendamento_repository.listar()
        )

        return len([
            a for a in agendamentos
            if a["status"] == "FALHA"
        ])