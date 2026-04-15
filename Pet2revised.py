import random
class Pet:
    def __init__(self, name, friendliness, hunger, bloodlust, thirst):
        self.name = name
        self.friendliness = friendliness
        self.hunger = hunger
        self.bloodlust = bloodlust
        self.thirst = thirst
y = random.randint(1,200) # Friendliness
w = random.randint(1,200) # Hunger
x = random.randint(1,10000) # Bloodlust
v = random.randint(1,200) # Thirst
MrBob = Pet('MrBob', y, w, x, v)
print(MrBob.name)
print("Friendliness:", y)
print("Hunger:", w)
print("Bloodlust:", x)
print("Thirst:", v)
z = input("Pet for friendliness, Feed for hunger, ")