import telebot
import massages
import database_relation

from telebot.types import BotCommand
from wiki import conf
from environs import Env

env = Env()
env.read_env()

token = env("BOT_TOKEN")
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def welcome_mass(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, massages.WELCOME)

    database_relation.upsert_user(chat_id, message.chat.first_name, message.chat.last_name)


@bot.message_handler(commands=['search'])
def welcome_mass(message):
    print('search started ...')

    chat_id = message.chat.id
    bot.send_message(chat_id, massages.SEARCH_TEXT)
    bot.register_next_step_handler_by_chat_id(chat_id, wiki_search_by_text)


def wiki_search_by_text(message):
    text = str(message.text).lower()
    chat_id = message.chat.id
    print('chat id ', chat_id)
    user_id = database_relation.get_user_id(chat_id)
    print("user_id ", user_id)

    link = database_relation.get_link_info(text)

    if link:
        print("link ", link)
        bot.send_message(chat_id, link.get('link'))
        database_relation.upsert_user_link(user_id.get('id'), link.get('id'))
    else:
        link_from_wiki = conf.WikiManager(text).get_result()
        if link_from_wiki:

            print('wiki is working ...')
            bot.send_message(chat_id=message.chat.id, text=link_from_wiki)
            database_relation.upsert_information(text, link_from_wiki)
        else:
            bot.send_message(chat_id=message.chat.id, text=massages.TEXT_NOT_FOUND)


def my_commands():
    return [
        BotCommand('/start', 'Boshlash'),
        BotCommand('/search', "Ma'lumot izlash"),

    ]


if __name__ == "__main__":
    print('started ...')
    bot.infinity_polling()
    bot.set_my_commands(my_commands())
