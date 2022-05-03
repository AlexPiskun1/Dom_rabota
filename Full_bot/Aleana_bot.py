# aleana_dostavka_bot
import telebot
from telebot import types
import key_bot

bot = telebot.TeleBot(key_bot.key_bot())


def kb_main(message, text = "Сделайте Ваш выбор"):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Контакты")
    button2 = types.KeyboardButton("Режим работы")
    button3 = types.KeyboardButton("Локация")
    button4 = types.KeyboardButton("Заказать доставку")
    kb.add(button1,button2,button3, button4)
    bot.send_message(message.chat.id,text,reply_markup=kb)

def kb_0(message, text = " Продолжайте работу "):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("  ")
    kb.add(button1)
    bot.send_message(message.chat.id,text,reply_markup=kb)

def kb_1(message, text = "Сделайте Ваш выбор"):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Кнопка4")
    button2 = types.KeyboardButton("Кнопка5")
    button3 = types.KeyboardButton("Кнопка6")
    kb.add(button1,button2,button3)
    bot.send_message(message.chat.id,text,reply_markup=kb)

def kb_inline_1(message, text = "Сделайте Ваш выбор"):
    kb = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("In1", callback_data="1-1")
    button2 = types.InlineKeyboardButton("In2", callback_data="1-2")
    button3 = types.InlineKeyboardButton("In2", callback_data="1-3")

    kb.add(button1,button2,button3)
    bot.send_message(message.chat.id, text, reply_markup=kb)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Добро день, {message.from_user.first_name}, Я помогу ВАМ оформить доставку")
    kb_main(message)



@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text.lower()
    try:
        if text in ["привет", "добрый день", "здоров", "hello", "hi"]:
            bot.send_message(message.chat.id, f"Добрый день,{message.from_user.first_name}, рад Вас слышать")
        elif text == 'admin':
            bot.send_message(message.chat.id, f"Добрый день,{message.from_user.first_name}, Вы вошли, как администратор")
        elif text == "контакты":
            bot.send_message(message.chat.id, f"A1 - +375(44)760-88-90\nМТС - +375(33)380-88-90\nгород - 8(01716)9-05-05\nсайт - aleana.by\ne-mail - weldbi@mail.ru")

        elif text == "режим работы":
            bot.send_message(message.chat.id, f"ПН-СУБ - 8.00-20.00\nВС - 9.00-18.00\nБез обеда")
            #kb_inline_1(message)


        elif text == "локация":
            bot.send_message(message.chat.id, f"г.Фаниполь, ул.Мира, 1А магазин Алеана\nкоординаты 53.75278, 27.33639")
        elif text in ["кнопка4","кнопка5","кнопка6"]:
            kb_main(message)


        else:
            bot.send_message(message.chat.id, f"{message.from_user.first_name}, сделайте свой выбор")

    except Exception:
        bot.send_message(message.chat.id, "Вы ввели некорректные данные")


@bot.message_handler(content_types=['sticker'])
def get_stiker(message):
    bot.send_message(message.chat.id, "Классный стикер! ")

@bot.callback_query_handler(func = lambda call: True)
def callback_InLine(call):
    if call.message:
        text = call.data
        if text == "1-1":
            bot.send_message(call.message.chat.id, "Ин кнопка1")
        else:
            bot.edit_message_text("ХЗ какая кнопка", call.message.chat.id,call.message.message_id, reply_markup=None) # изменяет сообщение ( удаляет клавиатуру)


bot.polling(none_stop=True)



bot.polling(none_stop=True)