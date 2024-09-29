import telebot
from telebot.types import Message
from telebot import types

bot = telebot.TeleBot("6408468484:AAGhSnw2ftzYASPwMxNgYXjx_UdoXTg1JaU")


@bot.message_handler(["start"])
def start(m: Message):
    bot.send_message(m.chat.id, f"Слушаю вас")


@bot.message_handler(content_types=["text"])
def math(m: Message):
    if m.text.lower().startswith("Математик"):
        bot.send_message(m.chat.id, "Ну че тебе надо?")
        bot.register_next_step_handler(m, math_hendler)


def math_hendler(m: Message):
    bot.send_message(m.chat.id, f"{eval(m.text)}")


bot.infinity_polling()
