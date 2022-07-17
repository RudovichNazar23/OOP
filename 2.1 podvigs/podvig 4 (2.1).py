class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

    def __check_money(self, money):
        self.__money = money
        if money >= 0 and isinstance(money, int):
            return True
        else:
            return False

mn_1 = Money(10)
mn_2 = Money(20)
print(mn_1.set_money(100))

