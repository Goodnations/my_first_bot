import telebot
import os  # Новая библиотека для работы с окружением

# Вместо старой строки с TOKEN пишем так:
# Берем токен из переменной окружения BOT_TOKEN
TOKEN = os.getenv('8665340788:AAHwaaGROrWrwxfjdOcaVKP0j9hmR2hOkYM')

# Важно: Добавим проверку, чтобы бот не запустился без токена
if TOKEN is None:
    print("ОШИБКА: Токен не найден! Установи переменную BOT_TOKEN.")
    exit() # Останавливаем программу, если токена нет

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот, написанный на телефоне, и теперь я живу в облаке!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Бот запущен и готов к переезду!")
bot.infinity_polling()