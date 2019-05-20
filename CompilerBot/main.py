import telebot
import requests
import configparser
import os

config_parser = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), 'config.cfg')
config_parser.read(config_file_path)
URL = config_parser.get('info', 'URL')
token = config_parser.get('info', 'token')
clientID = config_parser.get('info', 'clientID')
clientSecret = config_parser.get('info', 'clientSecret')

print(token)

if __name__ == '__main__':
    bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    params = {"script": message.text,
              "language": "cpp",
              "versionIndex": "0",
              "clientId": clientID,
              "clientSecret": clientSecret}
    r = requests.post(url=URL, json=params)
    if r.status_code == 200:
        data = r.json()
        bot.send_message(message.chat.id, 'Вывод: ' + data['output'])
    else:
        bot.send_message(message.chat.id, 'Ошибка')


bot.polling()

