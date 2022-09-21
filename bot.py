import telebot
from telebot import types
from config import TOKEN
from main import get_weather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    text = 'Я бот погоды, Отправь название города'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        text = get_weather(message.text)
        bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)


# Создать четыре кнопки с городами
#  При приветствии должен отправляться стикер
# После вывода погоды отправлять послесловие и стикер