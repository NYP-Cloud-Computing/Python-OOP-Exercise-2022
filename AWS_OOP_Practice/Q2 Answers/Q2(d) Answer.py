class Food:
    def __init__(self, name, price):
        self._name = name
        self._price = price


donut = Food("Chocolate Donut", 2.2)

print(donut._price)

donut.price = 2.5

print(donut._price)







