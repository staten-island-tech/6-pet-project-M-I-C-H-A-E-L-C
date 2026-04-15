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
if MrBob.name != 'MrBob':
    print("Not MrBob!")
else:
    print("MrBob!")
if MrBob.friendliness > 100:
    print("MrBob heppy")
else:
    print("MrBob angy")
    z = (input("pet MrBob to increase friendliness? yes - no: ")).upper()
    if z == "YES":
        print("MrBob heppy")
    else: 
        print("...")
if MrBob.hunger > 100:
    print("MrBob Hungy!")    
    m = input(("Feed MrBob? yes - no: ")).upper()
    if m == "YES":
        print("MrBob satisfied now")
    else: 
        print("...")
else:
    print("MrBob full")
if MrBob.bloodlust > 9000:
    print("MrBob sinister level over 9000! >:(")
    n = input(("Do something to fix MrBob? yes - no: ")).upper()
    if n == "YES":
        print("Innefective! MrBob doom coming!")
    else:
        print("Save us all.")
elif MrBob.bloodlust > 100:
    print("MrBob sinister  >_<")
    b = input(("Pet MrBob? yes - no: ")).upper()
    if b == "YES":
        print("MrBob kind (: ")
    else:
        print("...")
else:
    print("MrBob kind (: ")