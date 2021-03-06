from pyowm import OWM
import telebot
import key_weather

bot = telebot.TeleBot(key_weather.key_bot())

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать, я поГОДНЫЙ бот")



@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text.lower()
    try:
        if text in ["привет", "добрый день", "здоров", "hello", "hi"]:
            bot.send_message(message.chat.id, "Привет прямоходящий, ВВЕДИ название города")

        else:
            sity = str(text)
            owm = OWM(key_weather.key_w())
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(sity)
            w = observation.weather
            bot.send_message(message.chat.id, f"Температура: {w.temperature('celsius')['temp']} градусов \n Ветер: {w.wind()['speed']} м/с \n Облачность: {w.clouds} %")
    except Exception:
        bot.send_message(message.chat.id, "Вы неправильно ввели название города, введите еще раз")








bot.polling(none_stop=True)