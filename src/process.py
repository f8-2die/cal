import configparser
config = configparser.ConfigParser()
config.read("E:/git/cal/src/text.ini")
from src.сalculator import Calculator
class Process:
    def __init__(self):
        self.calculator = Calculator()
    def start(self):
        print(config.get("proc", "name"))
        self.first_number = int(input(config.get("proc", "first_number")))
        self.second_number = int(input(config.get("proc", "second_number")))
        self.choice = int(input(config.get("proc", "choice")))
        Process.solve(self)
    def solve(self):
        if self.choice == 1:
            self.calculator.sum(self.first_number, self.second_number)
        elif self.choice == 2:
            self.calculator.subtract(self.first_number, self.second_number)
        elif self.choice == 3:
            self.calculator.multiply(self.first_number, self.second_number)
        elif self.choice == 4:
            self.calculator.divide(self.first_number, self.second_number)
        elif self.choice == 5:
            self.calculator.square(self.first_number, self.second_number)
        else:
            print(config.get("proc", "false_num"))