import telebot
from telebot import types

api_token = '7216310296:AAFBjhO6ZNoY8Y8acdttYITYXs_QQHOuYrI'
bot = telebot.TeleBot(api_token)




@bot.message_handler(commands=['start','check'])
def handle_start(message):
    if message.text == '/check':
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        button1 = types.KeyboardButton('Записаться?')
        button2 = types.KeyboardButton('Отказаться!')
        keyboard.add(button1,button2)


        bot.reply_to(message,'Началась запись на занятия', reply_markup=keyboard)

        def all_check_message(message):

    else:
        bot.send_message(message.chat.id,'Записи пока нет')


#Создание кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    pass
    # if message.text == 'button 1':
    #     bot.reply_to(message,'A u ok?')









bot.polling(non_stop=True)