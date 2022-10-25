import telebot
import tg
from tg import getVotos

token = ' token da sua lata aqui, campeão.'

# aindo prefiro markdown, mas deixa assim mesmo.
bot = telebot.TeleBot(
   token, parse_mode="HTML"
)

# nao me pergunte pq eu fiz assim, quando eu tiver tempo eu melhoro isso.

@bot.message_handler(commands=["votos"])
def votos(message):
    resuts = getVotos()
    bot.reply_to(message, resuts)


bot.infinity_polling()
