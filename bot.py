import telebot
import tg
from tg import getVotos

bot = telebot.TeleBot(
    "5721885549:AAFTyeZfHoH7l34WgptlWq8TMhDG8gZRvq8", parse_mode="HTML"
)


@bot.message_handler(commands=["votos"])
def votos(message):
    resuts = getVotos()
    bot.reply_to(message, resuts)


print("What's going on here?")
print("Nada.")

bot.infinity_polling()
