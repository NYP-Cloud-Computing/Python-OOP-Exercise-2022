class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price  # Private attribute

    def get_price(self):
        return self.__price

    def get_price_discount(self):
        return f'The price of the donut after the discount is {self.__price}'

    def set_price(self, discount):
        self.__price = self.__price * discount


donut = Food("Chocolate Donut", 2.2)

print(donut.get_price())

donut.__price = 0

print(donut.get_price())

donut.set_price(0.5)

print(donut.get_price())

print(donut.get_price_discount())



