import telebot
from config import keys, TOKEN
from extensions import get_amount, get_currency,ConvertionException, CurrencyConverter
bot = telebot.TeleBot(TOKEN)


# обработка 2 основных команд
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Добро пожаловать!\nБот умеет конвертировать валюту!' \
           '\nПример сообщения для осуществления конвертации:' \
           '\n"5.99 долларов в рубли"\n\nПосмотреть список доступных валют: /values'
    # бот принимает 4 валюты: RUB, USD, EUR, CNY
    bot.reply_to(message, text)


# обработчик команды для получения списка валют
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        # непонятно почему именно text как переменная
        text = '\n- '.join((text, key))
    bot.reply_to(message, text)


# обработчик-приниматель сообщения с запросом на конвертацию
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        text = message.text.split()
        total_base = CurrencyConverter.convert(text)
    except ConvertionException as e:
        bot.reply_to(message, f'Не удалось обработать запрос 🤓 \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду со стороны программы!\n{e}')
    else:
        # это лучше в config
        text_2 = f'Цена {get_amount(text)} {keys[get_currency(text)[0]]} в {keys[get_currency(text)[-1]]} - {total_base * get_amount(text)}'
        bot.send_message(message.chat.id, text_2)


# запуск бота
bot.polling()