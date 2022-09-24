class Pokemon:
    def __init__(self, name, type, skill):  # attributes created in __init__ are called instance attributes
        # __init__ is a special kind of method that Python calls when it instantiates an object using the definitions found in a class
        self.name = name  # create attribute called name
        self.type = type
        self.skill = skill

    def __str__(self):
        return f'The pokemon {self.name} has the type {self.type} and skill {self.skill}'

    def attack(self, damage):
        return f'{self.name} attack using {self.skill} inflicting {damage} life points'


pikachu = Pokemon("Pikachu", "Electric", "Electric Bolt")  # Instantiate an object
meowth = Pokemon("Meowth", "normal", "Scratch")

print(pikachu.type)  # Access their instance attributes
print(meowth.skill)

pikachu.type = "fire"  # Values can be changed dynamically

print(pikachu.type)

print(pikachu.attack(10))

print(pikachu)

