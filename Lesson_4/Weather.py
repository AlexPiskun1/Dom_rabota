from pyowm import OWM

sity = str(input("Введите Ваш город"))
owm = OWM("85565fc28a37a2bdead37fe7ad01b0a3")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(sity)
w = observation.weather

print("Температура в ", sity, " : ",w.temperature('celsius')["temp"], "градусов")
print("Ветер в ", sity,": ",w.wind()["speed"], "м/с")
print("Облачность в ", sity,": ",w.clouds, "%")
