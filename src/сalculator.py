import configparser

config = configparser.ConfigParser()
config.read("E:/git/cal/src/text.ini")
res = config.get("cal", "res")

class Calculator:
    def sum(self, first_number, second_number):
        print(res, first_number + second_number)

    def subtract(self, first_number, second_number):
        print(res, first_number - second_number)

    def multiply(self, first_number, second_number):
        print(res, first_number * second_number)

    def divide(self, first_number, second_number):
        if second_number != 0:
            print(res, first_number / second_number)
        else:
            print(config.get("cal", "false_divide"))

    def square(self, first_number, second_number):
        print(config.get("cal", "res"), first_number ** second_number)