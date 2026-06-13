import pywhatkit
from datetime import datetime, timedelta
import time


class WhatsAppService:

    def enviar_mensagem(self, telefone, mensagem):

        try:
            # formato internacional Brasil
            if not telefone.startswith("+"):
                telefone = "+55" + telefone

            agora = datetime.now() + timedelta(minutes=1)

            hora = agora.hour
            minuto = agora.minute

            pywhatkit.sendwhatmsg(
                telefone,
                mensagem,
                hora,
                minuto,
                wait_time=10,
                tab_close=True
            )

            time.sleep(5)

            return True

        except Exception as e:
            print(f"Erro ao enviar WhatsApp: {e}")
            return False