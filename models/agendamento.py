class Agendamento:

    def __init__(
        self,
        contato_id,
        mensagem,
        data_envio,
        hora_envio,
        status="PENDENTE"
    ):

        self.contato_id = contato_id
        self.mensagem = mensagem
        self.data_envio = data_envio
        self.hora_envio = hora_envio
        self.status = status