from src.сalculator import Calculator

class Process:
    def __init__(self):
        self.calculator = Calculator()

    def start(self):
        print("Добро пожаловать в простой калькулятор")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        choice = int(input("Выберите, что хотите сделать с этими числами:\n1) Сложить\n2) Вычесть\n3) Умножить\n"
                           "4) Разделить\n5) Возвести в степень\nОперация: "))
        if choice == 1:
            self.calculator.sum(a, b)
        elif choice == 2:
            self.calculator.subtract(a, b)
        elif choice == 3:
            self.calculator.multiply(a, b)
        elif choice == 4:
            self.calculator.divide(a, b)
        elif choice == 5:
            self.calculator.square(a,b)
        else:
            print("Неправильно введена цифра")