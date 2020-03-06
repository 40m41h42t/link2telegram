# coding:utf-8

import telebot
import logging
from link2text import HTML2TelegramText
from telebot_setting import TOKEN
from telebot_setting import CHAT_ID
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handler_start_help(message):
    print(message)
    bot.reply_to(message, "Hello!")

@bot.message_handler(commands=['link'])
def handler_link(message):
    link_text = message.text[6:]
    ret_text = HTML2TelegramText(link_text)
    if ret_text == None:
        bot.reply_to(message, "Your Link is Invalid!")
        return
    # bot.send_message(message.chat.id, ret_text.encode(encoding='utf-8'), parse_mode='Markdown')
    bot.send_message(CHAT_ID, ret_text.encode(encoding='utf-8'), parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    test_id = message.forward_from_chat.id
    print(test_id)
    bot.reply_to(message, message.text)
    # bot.send_message(test_id, message.text)

if __name__ == '__main__':
    bot.polling()