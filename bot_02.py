# Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

# Definir Contatos para receber mensagem
prefixo = '+55'
estado = '83'

contatos = [ ]
mensagem = "TUTRA LELE"
# Definir intervalo de envio de mensagem 
 
    pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release("ctrl + w")

# Testar