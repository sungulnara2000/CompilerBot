import telebot
import requests


URL = "https://api.jdoodle.com/v1/execute"

bot = telebot.TeleBot('886490740:AAHCNylo55qhlWGcyiJ4fRe_u1Ov2AoK01M')

class Program:
    code = ''
    input = ''
    language = ''
    def __init__(self, language):
        self.language = language

program = Program('cpp')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['code'])
def get_code(message):
    bot.send_message(message.chat.id, 'Пришли мне свой код!')


@bot.message_handler(content_types=['text'])
def send_text(message):
        print(message.text)
        params = {"script": message.text,
                  "language": "cpp",
                  "versionIndex": "0",
                  # "stdin":
                  "clientId": "572a7d3d9dcafa3d2e7596e710656c70",
                  "clientSecret": "806d6ae46c4fc99e82c259b196c9ae0ee53ebf91ac0919519ad07cc9308dc1ab"}
        print(params)
        r = requests.post(url=URL, json=params)
        data = r.json()
        bot.send_message(message.chat.id, data['output'])

bot.polling()

