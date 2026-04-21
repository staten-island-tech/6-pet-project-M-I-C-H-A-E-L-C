import random
class Pet:
    def __init__(self, name, friendliness, hunger, bloodlust, thirst):
        self.name = name
        self.friendliness = friendliness
        self.hunger = hunger
        self.bloodlust = bloodlust
        self.thirst = thirst
f = random.randint(1,100) # Friendliness
h = random.randint(1,100) # Hunger
b = random.randint(1,100) # Bloodlust
t = random.randint(1,100) # Thirst
MrBob = Pet('MrBob', f, h, b, t)
print("MrBob")
print("😄", f, "🍖", h, "🤬", b , "💧", t)
while h >= 1 and t >= 1:
    if h <= 15:
        print("MrBob in critical hunger levels! Consider feeding")
    if t <= 15:
        print("MrBob in critical thirst levels! Consider feeding")
    x = input("Play, Feed, Give Water, Ignore: ").upper()
    if x == "PLAY":
        if h <= 30 and t <= 30:
            f -= 10
            print("😰")
        else:
            f += 10
        h -= 10
        b -= 10
        t -= 10
        print("😄🔺", f, "🍖🔻", h, "🤬🔻", b , "💧🔻", t)
    elif x == "FEED":
        print("😄🔺", f, "🍖🔺", h, "🤬🔻", b , "💧🔻", t)
    elif x == "Give Water":
        print("😄🔺", f, "🍖", h, "🤬🔻", b , "💧🔺", t)
    elif x == "Ignore":
        print("😄🔻", f, "🍖🔻", h, "🤬🔻", b , "💧🔻", t)
if h <= 1 or t <= 1:
    print("MrBob passed away from your negligence. Next time, watch him responsibly.")