import telebot
from telebot import types
bot = telebot.TeleBot("638688644:AAHL4FlM0InqWhi6WQCG4V1PVsiPO_w2fag")

environment = ['/QA','/CPC_QA', '/CPC_Production', '/Stage', '/Demo']


def key_board():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=e, callback_data=e) for e in environment]
    keyboard.add(*buttons)
    return keyboard

@bot.message_handler(commands=['build','Build','Hi'])
def handle_text(message):

    keyboard = key_board()
    if message.text == "/Hi":
        bot.send_message(message.chat.id, "Hello! I am NectainBOT. How can i help you?")

    elif message.text == "/Build" or message.text == "/build":

        bot.send_message(message.chat.id, "Choose environment :", reply_markup=keyboard)

    print message.text
@bot.message_handler(commands=['QA','CPC_QA', 'CPC_Producktion', 'Stage', 'Demo'])
def handle_environment(message):
    if message.text == "/QA":
        bot.send_message(message.chat.id, "Build and deploy to QA environment started")
    elif message.text == "/CPC_QA":
        bot.send_message(message.chat.id, "Build and deploy to CPC-QA environment started")
    elif message.text == "/CPC_Producktion":
        bot.send_message(message.chat.id, "Build and deploy to CPC-Producktion environment started")
    elif message.text == "/Stage":
        bot.send_message(message.chat.id, "Build and deploy to Stage environment started")
    elif message.text == "/Demo":
        bot.send_message(message.chat.id, "Build and deploy to Demo environment started")
    else:
        bot.send_message(message.chat.id, "Dont")
    print message.text
bot.polling(none_stop=True, interval=0)