from models.agendamento import Agendamento

from repositories.agendamento_repository import (
    AgendamentoRepository
)


class AgendamentoService:

    def __init__(self):

        self.repository = (
            AgendamentoRepository()
        )

    def criar_agendamento(
        self,
        contato_id,
        mensagem,
        data_envio,
        hora_envio
    ):

        agendamento = Agendamento(
            contato_id=contato_id,
            mensagem=mensagem,
            data_envio=data_envio,
            hora_envio=hora_envio
        )

        self.repository.criar(
            agendamento
        )

    def listar_agendamentos(self):

        return (
            self.repository.listar()
        )