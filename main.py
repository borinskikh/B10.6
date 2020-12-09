import telebot

token = "1420835702:AAGn-wPlzgNnqEnwSS4pzwlGF6t4xS4lAa8"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handleCommands(message):
    bot.reply_to(message, '/start')


@bot.message_handler(content_types=['text'])
def replyToMessage(message):
    bot.reply_to(message, "okay")


bot.polling()
