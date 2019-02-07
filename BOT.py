#(chat_id=-305397413)
import telebot
from telebot import types
from core import authentication



bot = telebot.TeleBot("638688644:AAHL4FlM0InqWhi6WQCG4V1PVsiPO_w2fag")
environment = ['/QA','/CPC_QA', '/CPC_Production', '/Stage', '/Demo']



def key_board():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=e, callback_data=e) for e in environment]
    keyboard.add(*buttons)
    return keyboard

@bot.message_handler(commands=['build','Build','Hi', "reg"])
def handle_text(message):
    keyboard = key_board()


    if message.text == "/Hi":
        bot.send_message(message.chat.id, "Hello! I am NectainBOT. How can i help you?")

    elif message.text == "/Build" or message.text == "/build":
        bot.send_message(message.chat.id, "Choose environment :", reply_markup=keyboard)
    elif message.text == "/reg":
        authentication.get_users_id(message, bot)
    print message.text
@bot.message_handler(commands=['QA','CPC_QA', 'CPC_Producktion', 'Stage', 'Demo'])
def handle_environment(message):

    if message.from_user.id in authentication.get_admin_ids(bot, message.chat.id):

        if message.text == "/QA":
            bot.send_message(message.chat.id, "Build and deploy to QA environment started")
        elif message.text == "/CPC_QA":
            bot.send_message(message.chat.id, "Build and deploy to CPC-QA environment started")
        elif message.text == "/CPC_Produktion":
            bot.send_message(message.chat.id, "Build and deploy to CPC-Production environment started")
        elif message.text == "/Stage":
            bot.send_message(message.chat.id, "Build and deploy to Stage environment started")
        elif message.text == "/Demo":
            bot.send_message(message.chat.id, "Build and deploy to Demo environment started")
    else:
      bot.send_message(message.chat.id, "Yuo don`t have permission to start build")
      print message.text
bot.polling(none_stop=True, interval=0)
