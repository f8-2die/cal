import os
from configparser import ConfigParser
config = ConfigParser()

config["proc"] = {
    "name": "Простой калькулятор",
    "first_number": "Введите первое число:",
    "second_number": "Введите второе число:",
    "choice": "Выберите, операцию\n1) Сложить\n2) Вычесть\n3) Умножить\n4) Разделить\n5) Возвести в степень\nОперация:",
    "false_num": "Неправильно введена цифра"
}
config["cal"] = {
    "res": f"Результат операции равен: ",
    "false_divide": f"Нельзя делить на 0!",
}

filename = os.path.join("E:\git\cal\src", "text.ini")
with open(filename, "w") as f:
    config.write(f)
