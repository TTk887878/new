import telebot
from telebot.types import InlineQuery, InlineQueryResultArticle as iqra, InputTextMessageContent as itmc
from telebot import types

bot = telebot.TeleBot("6408468484:AAGhSnw2ftzYASPwMxNgYXjx_UdoXTg1JaU")


@bot.inline_handler(func=lambda query: len(query.query) > 1)
def inline(query: InlineQuery):
    print(query.query)
    nums = query.query.split(" ")
    print(nums)
    if "x" in nums:
        if nums[1] == "+":
            e = nums[4] + "-" + nums[2]
        e = eval(e)
        urav = types.InlineQueryResultArticle('4', "уравнение",
                                              description=f"Результат;{e}",
                                              input_message_content=itmc(f"x={e}")
                                              )
        bot.answer_inline_query(query.id, [urav])
        return
    nums = tuple(map(float, nums))
    summ = sum(nums)
    diff = nums[0]
    mult = nums[0]
    q = nums[0]
    for el in nums[1:]:
        diff -= el
    for ef in nums[1:]:
        mult *= ef
    for ei in nums[1:]:
        q /= ei

    plus_icon = "https://pp.vk.me/c627626/v627626512/2a627/7dlh4RRhd24.jpg"
    minus_icon = "https://pp.vk.me/c627626/v627626512/2a635/ILYe7N2n8Zo.jpg"
    divide_icon = "https://pp.vk.me/c627626/v627626512/2a620/oAvUk7Awps0.jpg"
    multiply_icon = "https://pp.vk.me/c627626/v627626512/2a62e/xqnPMigaP5c.jpg"
    error_icon = "https://pp.vk.me/c627626/v627626512/2a67a/ZvTeGq6Mf88.jpg"
    new=''

    ant1 = iqra("1", "сумма", description=f"результат: {summ}", thumbnail_url=plus_icon,
                input_message_content=itmc(f"{nums[0]}{''.join([f' + {i}' for i in nums[1:]])} = {summ}"))
    ant2 = iqra("2", "разность", description=f"результат: {diff}", thumbnail_url=minus_icon,
                input_message_content=itmc(f"{nums[0]}{''.join([f' - {i}' for i in nums[1:]])} = {diff}"))
    ant3 = iqra("3", "произведение", description=f"результат: {mult}", thumbnail_url=multiply_icon,
                input_message_content=itmc(f"{nums[0]}{''.join([f' * {i}' for i in nums[1:]])} = {mult}"))
    ant4 = iqra("4", "частное", description=f"результат: {q}", thumbnail_url=divide_icon,
                input_message_content=itmc(f"{nums[0]}{''.join([f' / {i}' for i in nums[1:]])} = {q}"))
    bot.answer_inline_query(query.id, [ant1, ant2, ant3, ant4])




bot.infinity_polling()
