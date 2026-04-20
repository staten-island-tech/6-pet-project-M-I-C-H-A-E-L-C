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
    if MrBob.hunger <= 100:
        z = input("Feed Mr.Bob? ").upper()
        if z == "YES":
            y += 10 # Friendliness
            w += 10 # Hunger
            x -= 100 # Bloodlust
            v -= 10 # Thirst
            print("😄🔺", y, "🍖🔺", w, "🤬🔻", x , "💧🔻", v)
        elif z == "NO":
            print("...")
            y -= 10 # Friendliness
            x += 50 # Bloodlust
            print("😄🔻", y, "🍖", w, "🤬🔺", x , "💧", v)
        else:
            print("It's yes or no chud")
            z = input("Feed Mr.Bob? ").upper()
    elif MrBob.hunger >= 100:
        print("MrBob full")
        print("😄", y, "🍖", w, "🤬", x , "💧", v)
    n = input("Play with Mr.Bob? ").upper()
    if n == "YES":
        y += 10 # Friendliness
        w -= 10 # Hunger
        x -= 100 # Bloodlust
        v -= 10 # Thirst
        print("😄🔺", y, "🍖🔻", w, "🤬🔻", x , "💧🔻", v)
    elif n == "NO":
        print("...")
        y -= 10 # Friendliness
        x += 50 # Bloodlust
        print("😄🔻", y, "🍖", w, "🤬🔺", x , "💧", v)
    else:
        print("It's yes or no chud")
        n = input("Play with Mr.Bob? ").upper()
    if MrBob.friendliness >= 100:
        print("MrBob happy")
elif w < 0 or v < 0:
    print("MrBob ded")