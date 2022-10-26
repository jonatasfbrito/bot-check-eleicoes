import selenium
from selenium import webdriver
import time
from time import sleep


def getVotos():
    url = "https://resultados.tse.jus.br/oficial/app/index.html#/m/eleicao;e=e545/resultados"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1366,768")
    print("Full Screen: OK")
    nav = webdriver.Chrome("./chromedriver", chrome_options=options)
    nav.get(url)
    sleep(3)
    msg = nav.find_element("xpath", "/html/body")
    # secoes e dia
    secoes_totalizadas = msg.text.split("\n")[9]
    ultima_att = msg.text.split("\n")[12]

    # lula
    votos_lula = msg.text.split("\n")[15]
    por_lula = msg.text.split("\n")[16]

    # bolsonaro
    votos_bolsonaro = msg.text.split("\n")[19]
    por_bolsonaro = msg.text.split("\n")[20]

    if por_lula > por_bolsonaro:
        desc = f"""
=> SE PREPAREE!!!!


=> LULA NA FRENTE

1 => {por_lula} 🟥
2 => {por_bolsonaro} 🟩 
"""

    elif por_bolsonaro > por_lula:
        desc = f"""
=> ÉÉÉÉ BOLSONÁRIO!!!! PODEXA VAZÁ PODEXA VAZÁÁ!!!!


=> BOLSONARO NA FRENTE

1 => {por_bolsonaro}🟩
2 => {por_lula} 🟥
"""
    else:
        desc = f"""
=> TAPORRA DUELO DE TITÃNS KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK

=> EMPATE

0 => {por_bolsonaro}🟩  
0 => {por_lula} 🟥
"""

    return desc
    nav.quit()
    print('Terminei a request, organizei os dados e enviei a mensagem!!')
