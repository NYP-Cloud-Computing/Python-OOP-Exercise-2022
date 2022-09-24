class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price


donut = Food("Chocolate Donut", 2.2)

print(donut.get_price())









