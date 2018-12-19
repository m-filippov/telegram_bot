import telebot
from telebot import types
bot = telebot.TeleBot("Token")

environment = ['/QA','/CPC_QA', '/CPC_Producktion', '/Stage', '/Demo']

def check_environment(message):
    for e in environment:
        if e in message.text:
            handle_environment(e)
            print e

def key_board():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=e, callback_data=e) for e in environment]
    keyboard.add(*buttons)
    return keyboard
#/@bot.callback_query_handler(func=lambda x: True)
#def callback_handler(callback_query):

#    message = callback_query.message
#    text = callback_query.data
#    if message == "QA":
#        bot.answer_callback_query(callback_query_id=callback_query.id,
#                                  text="Build and deploy to QA environment started")
#    elif text == "CPC-QA":
#        bot.answer_callback_query(callback_query_id=callback_query.id,
#                                  text="Build and deploy to CPC-QA environment started")
#    elif text == "CPC-Producktion":
#        bot.answer_callback_query(callback_query_id=callback_query.id,
#                                  text="Build and deploy to CPC-Producktion environment started")
#    elif text == "Stage":
#        bot.answer_callback_query(callback_query_id=callback_query.id,
#                                  text="Build and deploy to Stage environment started")
#    elif text == "Demo":
#        bot.answer_callback_query(callback_query_id=callback_query.id,
#                                  text="Build and deploy to Demo environment started")
#
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
