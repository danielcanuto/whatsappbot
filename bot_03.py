# Importar bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar ate o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(60)

#Definir contatos ou grupos e mensgem a ser enviadas
contatos = ["AlohaClan", "Os Larôtxas"]
# buscar contatos ou grupos
# <div class="_1awRl copyable-text selectable-text" contenteditable="true" data-tab="3" dir="ltr"></div>
# <div class="_1awRl copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div>
mensagem = " Visite o https://alohaclan.com/"
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    time.sleep(2)
    campo_pesquisa.send_keys(contato)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(3)
    


def enviar_msg(mensagem):
    campo_msg = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    
    time.sleep(2)
    campo_msg[1].send_keys(mensagem)
    time.sleep(3)
    campo_msg[1].send_keys(Keys.ENTER)

def enviar_img(img):
    # <span data-testid="clip" data-icon="clip" class=""></span>
    pass


for contato in contatos:
    buscar_contato(contato)
    enviar_msg(mensagem)



# def msg_grupo

