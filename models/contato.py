class Contato:
    def __init__(
        self,
        nome,
        telefone,
        empresa="",
        observacoes="",
        id=None
    ):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.observacoes = observacoes
        