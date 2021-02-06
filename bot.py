from selenium import webdriver
import time

class WhatsAppBot:
    def __init__(self):
        self.mensagem = "Bom dia Aloha - visite nosso site https://alohaclan.com/"
        self.grupos = ["AlohaClan", "Larôtxas"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="AlohaClan" class="_1hI5g _1XH7x _1VzZY"><span class="matched-text _1VzZY">Al</span>ohaClan</span>
        # <div tabindex="-1" class="DuUXI">
        # <span data-testid="send" data-icon="send" class="">
        # 

        self.driver.get("https://web.whatsapp.com/")
        time.sleep(20)
        # self.driver.find_element_by_xpath()
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(4)
            grupo.click()

            chat_box = self.driver.find_elements_by_class_name('DuUXI')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-ico="send"]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(4)


bot = WhatsAppBot()
bot.EnviarMensagens()