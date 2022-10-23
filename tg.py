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
    sleep(5)
    msg = nav.find_element("xpath", "/html/body")
    print(msg.text)
    # secoes e dia
    secoes_totalizadas = msg.text.split("\n")[9]
    ultima_att = msg.text.split("\n")[12]

    # lula
    votos_lula = msg.text.split("\n")[15]
    por_lula = msg.text.split("\n")[16]

    # bolsonaro
    votos_bolsonaro = msg.text.split("\n")[19]
    por_bolsonaro = msg.text.split("\n")[20]

    resultados = f"""

<b>SEÇÕES TOTALIZADAS</b>: <pre>{secoes_totalizadas}</pre>
<b>ÚLTIMA ATUALIZAÇÃO</b>: <pre>{ultima_att}</pre>

<b>LULA</b>: <pre>{por_lula}</pre> => <pre>{votos_lula}%</pre> <b>dos votos.</b>

VS

<b>BOLSONARO</b>: <pre>{por_bolsonaro}</pre> => <pre>{votos_bolsonaro}%</pre> <b>dos votos.</b>
"""
    return resultados
    nav.quit()
