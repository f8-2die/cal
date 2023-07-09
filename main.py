#самый тупой калькулятор детсадовского уровня из спец группы для умственно отсталых
while True:#бесконечный цикл

    num1 = float(input("Введите первое число: ")) #делаем в начале флоат, иначе будет str
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /, ^): ") #ждем на вход символ операции

    # Выполнение тупых операции и вывод не менее тупого результата
    if operation == '+':
        result = num1 + num2
    elif operation == '-': #у нормальных поцанов else if
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("на ноль делить нельзя, дибил")
            continue
    elif operation == '^':
        result = num1 ** num2
    else:
        print("Ошибка: даже выбрать из предложенного не можешь, кто еще тут даун")
        continue

    print("Результат:", result)

    # Запрос продолжения работы
    answer = input("Хотите продолжить работу? (да/нет): ")
    if answer.lower() == 'да':
        continue
    else:
        break