import telebot
import json
import requests

token = "1420835702:AAGn-wPlzgNnqEnwSS4pzwlGF6t4xS4lAa8"

bot = telebot.TeleBot(token)

rates = json.loads(requests.get(
    'https://api.exchangeratesapi.io/latest').text)['rates']


@bot.message_handler(commands=['start', 'help'])
def handleCommands(message):
    bot.send_message(message, rates)


@bot.message_handler(content_types=['text'])
def replyToMessage(message):
    input = message.text.split()
    if len(input) == 3 and input[0].isdigit() and input[1].isalpha() and input[2].isalpha():

        output = str(rates[input[1]]) + ' ' + str(rates[input[2]])
        bot.send_message(message.chat.id, output)
    else:
        bot.send_message(message.chat_id, 'Wrong formatting')


bot.polling()
