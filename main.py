import telebot
bot = telebot.TeleBot('6814431946:AAHkEPWcbHhTJ5xHY46H4ZUnhQ0OyuWESsE')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Здравствуйте!* \nЭто мой первый бот', parse_mode='Markdown')

@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, '_Спасибо, что написали_', parse_mode='Markdown')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Чтобы посмотреть мультфильм, пройдите по [ССЫЛКЕ] (https://yandex.ru/video/preview/17504070381261047229)', parse_mode='Markdown')

bot.infinity_polling()