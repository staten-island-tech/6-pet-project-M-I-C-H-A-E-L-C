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
        print("MrBob in critical thirst levels! Consider giving water")
    print("Command")
    print("Play")
    print("Feed")
    print("Give Water")
    print("Ignore")
    x = input(": ").upper()
    if x == "PLAY":
        if h <= 30 or t <= 30:
            f -= 10
            print("😰 MrBob no want to play anymore")
            print("😄🔻", f, "🍖🔻", h, "🤬🔻", b , "💧🔻", t)
        else:
            f += 10
            print("😄🔺", f, "🍖🔻", h, "🤬🔻", b , "💧🔻", t)
        h -= 10
        b -= 10
        t -= 10
    elif x == "FEED":
        f += 10
        h += 10
        b -= 10
        t -= 10
        print("😄🔺", f, "🍖🔺", h, "🤬🔻", b , "💧🔻", t)
    elif x == "GIVE WATER":
        f += 10
        h -= 5
        b -= 10
        t += 20
        print("😄🔺", f, "🍖", h, "🤬🔻", b , "💧🔺", t)
    elif x == "IGNORE":
        f -= 10
        h -= 10
        b += 50
        t -= 10
        print("😄🔻", f, "🍖🔻", h, "🤬🔻", b , "💧🔻", t)
    if b >= 100:
        print("MR BOB SINISTER WE'RE DOOMEDDDD")
        break
if h <= 1 or t <= 1:
    print("MrBob passed away from your negligence. Next time, watch him responsibly.")