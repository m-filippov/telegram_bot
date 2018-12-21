import re



def get_users_id(message, bot):
    user_id = str(message.chat.id)

    with open('C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\Users_id', "r",) as f:
        for line in f:
            print line
        if user_id in line:
                bot.send_message(message.chat.id, "User already exist")

        else:
            with open('C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\Users_id', "a", ) as fi:
                fi.write(user_id+"\n")
            bot.send_message(message.chat.id, "User add owner")
            print user_id

def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
