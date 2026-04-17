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
print("😄", y, "🍖", w, "🤬", x , "💧", v)
if w >= 0 and v >= 0:
 #   m = input("Give MrBob water? ")
    z = input("Feed Mr.Bob? ").upper()
    if z == "YES":
        y += 10
        w += 10
        x -= 100
        v -= 10
        print("😄", y, "🍖", w, "🤬", x , "💧", v)
    if z == "NO":
        print("...")
        print("😄", y, "🍖", w, "🤬", x , "💧", v)
    if MrBob.hunger >= 100:
        print("MrBob full")
    n = input("Play with Mr.Bob? ").upper()
    if n == "YES":
        y += 10
        w -= 10
        x -= 100
        v -= 10
        print("😄", y, "🍖", w, "🤬", x , "💧", v)
    if n == "NO":
        print("...")
        y -= 10
        x += 50
        print("😄", y, "🍖", w, "🤬", x , "💧", v)
    if MrBob.friendliness >= 100:
        print("MrBob happy")