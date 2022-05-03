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
    kb = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Машина до 1т, до 4 м3", callback_data="1")
    button2 = types.InlineKeyboardButton("Машина до 3.5т, до 18м3", callback_data="2")
    button3 = types.InlineKeyboardButton("Манипулятор до 10т, 8 под", callback_data="3")

    kb.add(button1,button2,button3)
    bot.send_message(message.chat.id, text, reply_markup=kb)

def kb_inline_time(message, text = "Выбирите время"):
    kb = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("9.00-10.00", callback_data="9")
    button2 = types.InlineKeyboardButton("10.00-11.00", callback_data="10")
    button3 = types.InlineKeyboardButton("11.00-12.00", callback_data="11")
    button4 = types.InlineKeyboardButton("12.00-13.00", callback_data="12")
    button5 = types.InlineKeyboardButton("13.00-14.00", callback_data="13")
    button6 = types.InlineKeyboardButton("14.00-15.00", callback_data="14")
    button7 = types.InlineKeyboardButton("15.00-16.00", callback_data="15")
    button8 = types.InlineKeyboardButton("16.00-17.00", callback_data="16")
    button9 = types.InlineKeyboardButton("17.00-18.00", callback_data="17")
    button10 = types.InlineKeyboardButton("18.00-19.00", callback_data="18")
    button11 = types.InlineKeyboardButton("19.00-20.00", callback_data="19")

    kb.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11)
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
            bot.send_message(message.chat.id, f"г.Фаниполь, ул.Мира, 1А\nМагазин Алеана\nкоординаты 53.75278, 27.33639")
        elif text == "заказать доставку":
            kb_inline_1(message)


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
        if text == "1":
            bot.send_message(call.message.chat.id, "Форд Транзин АН5885-5 приедет к Вам")
            kb_inline_time(call.message)
        elif text == "2":
            bot.send_message(call.message.chat.id, "Мерседес АВ4697-5 приедет к Вам")
            kb_inline_time(call.message)
        elif text == "3":
            bot.send_message(call.message.chat.id, "Манипулятор Скания АТ2657-5 приедет к Вам")
            kb_inline_time(call.message)
        else:
            bot.edit_message_text("ХЗ какая кнопка", call.message.chat.id,call.message.message_id, reply_markup=None) # изменяет сообщение ( удаляет клавиатуру)


bot.polling(none_stop=True)



bot.polling(none_stop=True)