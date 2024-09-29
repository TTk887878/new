import telebot
from telebot import types
from telebot.types import InlineKeyboardButton as IB, Message,CallbackQuery

TOKEN = "6894315268:AAHBNpkznkxDD9ghpRyXILUgzE_EPIUcgCU"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(m: Message):
    kb = types.InlineKeyboardMarkup()
    kb.row(IB("google", url="google.com"))
    kb.row(IB(text="yandex", url="yandex.ru"))
    bot.send_message(m.chat.id, text="какую сторону выберешь путник", reply_markup=kb)


def inline():
    kb = types.InlineKeyboardMarkup()
    kb.row(IB("1", callback_data="1"), IB(text="2", callback_data="ghg"))
    kb.row(IB(text=3,callback_data="3"))

    return kb


@bot.message_handler(commands=["button"])
def button(m: Message):
    bot.send_message(m.chat.id, text="в прошлый раз ты выбрал скользкую дорожку на этот раз не ошибись",
                     reply_markup=inline())


@bot.callback_query_handler(func=lambda call:True)
def call_back(c:CallbackQuery):
    if c.data=="1":
        start(c.message)
    elif c.data=="ghg":
        bot.send_message(c.message.chat.id,text="я валера")
    elif c.data=="3":
        bot.send_message(c.message.chat.id,text="я джокер виктор дудка")



n=0
@bot.message_handler(commands=["neLoveMath"])
def nn(m:Message):
    bot.send_message(m.chat.id,text="мне нужна твоя одежда мотоцикл и число от 1 до 100")
    bot.register_next_step_handler(m,reg1)


def reg1(m:Message):
    global n
    n=int(m.text)
    if n not in range(1,101):
        bot.send_message(m.chat.id,text="ты помойму перепутал")
        nn(m)
        return
    bot.send_message(m.chat.id, text="мне нужен твой мотоцикл одежда и второе число от 1 до 100")
    bot.register_next_step_handler(m,reg2)


def reg2(m:Message):
    b=int(m.text)
    if b not in range(1,101):
        bot.send_message(m.chat.id,text="ты помойму перепутал")
        reg1(m)
        return
    bot.send_message(m.chat.id,f"результат возведения в степень={n**b}")




bot.polling(non_stop=True)
