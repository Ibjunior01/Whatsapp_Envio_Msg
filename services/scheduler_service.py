import threading
import time
from datetime import datetime
from services.agendamento_service import (AgendamentoService)
from services.whatsapp_service import (WhatsAppService)


class SchedulerService:

    def __init__(self):

        self.agendamento_service = (
            AgendamentoService()
        )

        self.whatsapp_service = (
            WhatsAppService()
        )

    def iniciar(self):

        thread = threading.Thread(
            target=self.executar,
            daemon=True
        )

        thread.start()

    def executar(self):

        print("Thread criada")

        while True:

            try:

                pendentes = (
                    self.agendamento_service
                    .listar_pendentes()
                )

                print(
                    f"Pendentes encontrados: {len(pendentes)}"
                )

                for agendamento in pendentes:

                    data_hora_agendada = datetime.strptime(
                        f"{agendamento['data_envio']} {agendamento['hora_envio']}",
                        "%Y-%m-%d %H:%M"
                    )

                    agora = datetime.now()

                    print(
                        f"Agendado: {data_hora_agendada}"
                    )

                    print(
                        f"Agora: {agora}"
                    )

                    if agora >= data_hora_agendada:

                        print(
                            f"ENVIANDO -> {agendamento['nome']}"
                        )

                        telefone = agendamento["telefone"]

                        mensagem = agendamento["mensagem"]

                        sucesso = (
                            self.whatsapp_service
                            .enviar_mensagem(
                                telefone,
                                mensagem
                            )
                        )

                        if sucesso:

                            self.agendamento_service.atualizar_status(
                            agendamento["id"],
                            "ENVIADO"
                        )
                        
                            print(
                                f"ENVIADO -> {agendamento['nome']}"
                            )   

                        else:

                            print(
                                f"FALHA -> {agendamento['nome']}"
                            )

                    else:

                        print(
                            f"Aguardando horário -> {agendamento
                            ['nome']}"
                        )

            except Exception as e:

                print(
                    f"Erro Scheduler: {e}"
                )


            time.sleep(10)