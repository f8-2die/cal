class Calculator:
    def sum(self, a, b):
        print(f"Результат операции {a} + {b} равен {a + b}")

    def subtract(self, a, b):
        print(f"Результат операции {a} - {b} равен {a - b}")

    def multiply(self, a, b):
        print(f"Результат операции {a} * {b} равен {a * b}")

    def divide(self, a, b):
        if b != 0:
            print(f"Результат операции {a} / {b} равен {a / b}")
        else:
            print("Нельзя делить на 0!")
    def square(self,a, b):
        print(f"Результат операции {a}^{b} равен {a ** b}")