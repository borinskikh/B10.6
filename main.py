import telebot
from extensions import Price


bot = telebot.TeleBot(open("token", "r").read())
bot.polling()


@bot.message_handler(commands=['start', 'help'])
def startCommands(message):
    pass


@bot.message_handler(commands=['values'])
def valuesCommand(message):
    pass


@bot.message_handler(content_types=['text'])
def replyToMessage(message):
    try:
        output = Price.get_price(message)
    except Exception as e:
        output = e
    bot.send_message(message.chat.id, output)
