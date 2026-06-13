from services.agendamento_service import (
    AgendamentoService
)

service = AgendamentoService()

for item in service.listar_agendamentos():
    print(dict(item))