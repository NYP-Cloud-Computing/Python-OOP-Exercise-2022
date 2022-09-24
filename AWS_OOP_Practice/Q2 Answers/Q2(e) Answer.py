class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


donut = Food("Chocolate Donut", 2.2)

print(donut.__price)

donut.price = 2.5

print(donut.__price)







