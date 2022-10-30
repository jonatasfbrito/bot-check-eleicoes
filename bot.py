# importei as biblioteca tudo ne ta ligadokkkkkkkk
import telebot
import tg
from tg import getVotos
import time
import datetime

# Cria o loop
while True:
    # aqui ele vai ver se a data de hoje é
    # o dia do segundo turno
    if datetime.date.today() == '2022-10-30':
        print('As eleições ainda não se iniciaram. Repassando!!!')
        time.sleep(1000)
        # depois daqui ele vai repetir o processo ate dar dia 30
    else:
        # ele ta ligado que é dia 30, entao
        # ja vai pegando o resultado dos votos
        # e criando a instancia do bot
        print('Executando..')
        time.sleep(12)
        cid = -1001577196038
        bot = telebot.TeleBot("5721885549:AAFTyeZfHoH7l34WgptlWq8TMhDG8gZRvq8")
        resuts = getVotos()
        bot.send_message(cid, 'ENVIANDO ATUALIZAÇÃO DAS ELEIÇÕES!! AGUAREM!! ( 20s )')
        # cara essa parte me quebrou -
        # legal pqp KKKKKKKKKKKKKKKK -
        # rachei mt
        if 'LULA NA FRENTE' in resuts:
            audio = open('./audios/lula_se_preparem.mp3','rb')
            bot.send_chat_action(cid, 'record_audio')
            bot.send_audio(cid, audio, caption=resuts)
        elif 'BOLSONARO NA FRENTE' in resuts:
            audio = open('./audios/bolsonaro_deixa_derramar.mp3','rb')
            bot.send_chat_action(cid, 'record_audio')
            bot.send_audio(cid, audio, caption=resuts)
        elif 'EMPATE' in resuts:
            bot.send_chat_action(cid, 'record_audio')
            audio = open('./audios/duelo.mp3','rb')
            bot.send_audio(cid, audio, caption=resuts)

