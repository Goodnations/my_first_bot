import telebot
import os  # Новая библиотека для работы с окружением

# Вместо старой строки с TOKEN пишем так:
# Берем токен из переменной окружения BOT_TOKEN
TOKEN = os.getenv('BOT_TOKEN')

# Важно: Добавим проверку, чтобы бот не запустился без токена
if TOKEN is None:
    print("ОШИБКА: Токен не найден! Установи переменную BOT_TOKEN.")
    exit() # Останавливаем программу, если токена нет

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот, написанный на телефоне, и теперь я живу в облаке!")

@bot.message_handler(func=lambda message: True)
def answer(message):
    text = message.text.lower()  # приводим текст к нижнему регистру для удобства

    if text == "привет":
        bot.reply_to(message, "Привет! Как дела?")
    elif text == "пока":
        bot.reply_to(message, "До свидания! Заходи ещё.")
    elif text == "/help":
        bot.reply_to(message, "Я понимаю команды: /start, /help, а также слова 'привет' и 'пока'.")
    else:
        # Если ничего не подошло, просто повторяем (как раньше)
        bot.reply_to(message, message.text)

print("Бот запущен и готов к переезду!")
bot.infinity_polling()