import types
import random

import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('234234')


# старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Обо мне')
    btn2 = types.KeyboardButton('Мои проекты')
    btn3 = types.KeyboardButton('Генератор чисел🎰')
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}✋', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    # обо мне
    # todo текстовки в объект
    if message.text == 'Обо мне':
        bot.send_message(message.chat.id, 'Привет, рад что ты посетил моего бота!😊')
        bot.send_message(message.chat.id, 'Меня зовут Ваня, я учусь в 8 классе и увлекаюсь программированием‍💻')
        bot.send_message(message.chat.id, 'В будущем хочу связать с ним жизнь.👨🏻‍💻')
        bot.send_message(message.chat.id, 'Очень люблю баскетбол и всё, что с ним связано🏀')
        bot.send_message(message.chat.id, 'Хорошо разбираюсь в математике и информатике🔢')
        bot.send_message(message.chat.id, 'Если есть лишняя копеечка можешь поддержать мои старания тут⬇️')
        bot.send_message(message.chat.id, ' https://www.donationalerts.com/r/theperfusha 💸')
        bot.register_next_step_handler(message, on_click)
    # мои проекты
    elif message.text == 'Мои проекты':
        bot.send_message(message.chat.id, 'Пока что здесь пусто😞')
        bot.register_next_step_handler(message, on_click)
    # генератор чисел
    elif message.text == 'Генератор чисел🎰':
        l: list[1] = list(range(1, 101))
        random.shuffle(l)
        for i in l:
            bot.send_message(message.chat.id, f'Сгенерированное число: {i}')
            break
        bot.register_next_step_handler(message, on_click)

    # сайт


@bot.message_handler(commands=['site', 'website'])
def start(message):
    bot.send_message(message.chat.id, 'в будующем сдесь что-то будет🐭')
    bot.register_next_step_handler(message, on_click)

    # помощь


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Нужна помощь? Пиши сюда => <u>@Vanya_PerF1LLLY</u> ✉', parse_mode='html')
    bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
