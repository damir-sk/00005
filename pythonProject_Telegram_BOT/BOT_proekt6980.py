#при вводе в телеграм должен учитывать кол-во валюты

import telebot
from  config import keys, TOKEN
from prilogenie import ConvertionException,MoneyConverter

bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(content_types=['photo', "text", 'voice'])
#def repeat(message: telebot.types.Message):
#    bot.reply_to(message, 'hi, Nice day')

#bot.polling(none_stop=True)
#говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.



@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
     text = 'Чтобы начать введите команду в следующем формате: <имя валюты>, <в какую валюту переводим>, <количество валюты>\n Чтобы увидеть полный список валют Введите: /values'
     bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
           text='\n'.join((text, key, ))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):

    try:
        values = message.text.split (' ')

        if len (values) != 3:
            raise ConvertionException ('Слишком много параметров')  # Ошибки пользователя
        # (доллар  рубль    1 )
        quote, base, amount = values

        total_base = MoneyConverter.convert (quote, base, amount)
    except ConvertionException as e:
        bot.reply_to (message, f'Пользователь ошибся при вводе\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:

        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id,text)

     #bot.reply_to(message, text)



bot.polling(none_stop=True)