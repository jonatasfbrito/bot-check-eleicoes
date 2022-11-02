
import selenium
from selenium import webdriver
import time
from time import sleep

def getVotos():
    url = "https://resultados.tse.jus.br/oficial/app/index.html#/m/eleicao;e=e545/resultados"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1366,768')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--lang=pt-BR')
    nav = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    nav.get(url)
    sleep(15)
    msg = nav.find_element("xpath", "/html/body")
    # secoes e dia
    print(msg.text)
    secoes_totalizadas = msg.text.split("\n")[10]
    ultima_att = msg.text.split("\n")[13]
    # lula
    votos_lula = msg.text.split("\n")[15]
    por_lula = msg.text.split("\n")[16]

    # bolsonaro
    votos_bolsonaro = msg.text.split("\n")[19]
    por_bolsonaro = msg.text.split("\n")[20]

    if votos_lula > votos_bolsonaro:
        desc = f"""
LULA NA FRENTE

seções totalizadas: {secoes_totalizadas}
atualizado em: {ultima_att}


1 => {por_lula} 🟥
2 => {por_bolsonaro} 🟩 
"""

    elif votos_lula < votos_bolsonaro:
        desc = f"""
BOLSONARO NA FRENTE

seções totalizadas: {secoes_totalizadas}
atualizado em: {ultima_att}

1 => {por_bolsonaro}🟩
2 => {por_lula} 🟥
"""
    else:
        desc = f"""
DUELO DE TITANS

0 => {por_bolsonaro}🟩  
0 => {por_lula} 🟥
"""

    return desc
    nav.quit()
