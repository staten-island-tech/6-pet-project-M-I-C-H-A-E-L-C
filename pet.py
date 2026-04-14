import random
class Pet:
    def __init__(self, name, friendliness, hunger, bloodlust, thirst):
        self.name = name
        self.friendliness = friendliness
        self.hunger = hunger
        self.bloodlust = bloodlust
        self.thirst = thirst
x = random.randint(1,10000)
y = random.randint(1,200)
MrBob = Pet('MrBob', y, 90, x, 35)
if MrBob.friendliness > 100:
    print("MrBob heppy")
else:
    print("MrBob angy")
if MrBob.hunger > 100:
    print("MrBob Hungy!")
else:
    print("MrBob Satisfied")
if MrBob.bloodlust > 9000:
    print("MrBob sinister level over 9000! >:(")
elif MrBob.bloodlust > 100:
    print("MrBob sinister  >_<")
else:
    print("MrBob kind (: ")
z = input("pet MrBob to increase friendliness? Yes - No")
if z == "Yes":
    y.append(MrBob.friendliness) 