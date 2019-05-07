import telebot
import requests


URL = "https://api.jdoodle.com/v1/execute"

bot = telebot.TeleBot('886490740:AAHCNylo55qhlWGcyiJ4fRe_u1Ov2AoK01M')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def send_text(message):
        print(message.text)
        PARAMS = {"script": message.text,
                  "language": "cpp",
                  "versionIndex": "0",
                  "clientId": "572a7d3d9dcafa3d2e7596e710656c70",
                  "clientSecret": "806d6ae46c4fc99e82c259b196c9ae0ee53ebf91ac0919519ad07cc9308dc1ab"}
        print(PARAMS)
        r = requests.post(url=URL, json=PARAMS, verify=False)
        data = r.json()
        bot.send_message(message.chat.id, data['output'])

bot.polling()

