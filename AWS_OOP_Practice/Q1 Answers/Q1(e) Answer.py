class Pokemon:
    def __init__(self, name, type, skill):  # attributes created in __init__ are called instance attributes
        # __init__ is a special kind of method that Python calls when it instantiates an object using the definitions found in a class
        self.name = name  # create attribute called name
        self.type = type
        self.skill = skill

    def attack(self, damage):
        return f'{self.name} attack using {self.skill} inflicting {damage} life points'


pikachu = Pokemon("Pikachu", "Electric", "Electric Bolt")  # Instantiate an object

print(pikachu.type)  # Access their instance attributes
print(pikachu.skill)

pikachu.skill = "Iron Tail"  # Values can be changed dynamically

print(pikachu.skill)
print(pikachu.attack(10))