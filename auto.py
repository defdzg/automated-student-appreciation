from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ApreciacionBot:
    def __init__(self,clave,unip,correo):
        self.clave = clave
        self.unip = unip
        self.correo = correo
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('http://dep.uaemex.mx/apreciacion/')
        time.sleep(1)
        clave = bot.find_element_by_name('clave')
        clave.clear()
        clave.send_keys(self.clave)
        time.sleep(1)
        unip = bot.find_element_by_name('unip')
        unip.clear()
        unip.send_keys(self.unip)
        time.sleep(1)
        '''correo = bot.find_element_by_name('correo')
        correo.clear()
        correo.send_keys(self.correo)
        time.sleep(1)'''
        ingresar = bot.find_element_by_name('btn').click()
        time.sleep(1)
        iniciar = bot.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[3]/tbody/tr[1]/td/a').click()

    def encuesta(self):
        bot = self.bot
        for y in range(2,15):
            for x in range(2,14):
                if y < 8:
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()  
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:       
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[4]'
                        answer = bot.find_element_by_xpath(xpath).click()
                if y > 9:
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[6]'
                        answer = bot.find_element_by_xpath(xpath).click()
        for y in range(16,21):
            for x in range(2,14):
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[6]'
                        answer = bot.find_element_by_xpath(xpath).click()
        for y in range(22,27):
            for x in range(2,14):
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[6]'
                        answer = bot.find_element_by_xpath(xpath).click()
        for y in range(28,35):
            for x in range(2,14):
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[6]'
                        answer = bot.find_element_by_xpath(xpath).click()
        for y in range(36,41):
            for x in range(2,14):
                    if x == 5:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    elif x == 6:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[3]'
                        answer = bot.find_element_by_xpath(xpath).click()
                    else:
                        xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/div/table['+str(y)+']/tbody/tr[2]/td/table/tbody/tr['+str(x)+']/td[6]'
                        answer = bot.find_element_by_xpath(xpath).click()

cta = ...
unip = ...
correo = ...       
test = ApreciacionBot(cta,unip, correo)
test.login()
test.encuesta()
