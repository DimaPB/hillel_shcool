# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121
# які діляться націло на 3 та на 2
#
# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення -
# звичайні методи.I зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.
#
# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
# до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
# Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення
# в файл коли ми запустили тест та текстове повідомлення що ми стартанули.
# Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
# використайте вже відому вам бібліотеку дататайм

number = [i for i in range(34, 121) if i % 2 == 0 and i % 3 == 0]
print(number)


class Calculator:
    def adding(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplying(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    @staticmethod
    def message():
        print("Привіт я калькулятор")