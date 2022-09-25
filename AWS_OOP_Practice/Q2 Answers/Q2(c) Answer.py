class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


donut = Food("Chocolate Donut", 2.2)

print(donut.price)

donut.price = 2.5

print(donut.price)







