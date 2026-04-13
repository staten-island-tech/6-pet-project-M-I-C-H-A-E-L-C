class Pet:
    def __init__(self, name, friendliness, hunger, bloodlust, thirst):
        self.name = name
        self.friendliness = friendliness
        self.hunger = hunger
        self.bloodlust = bloodlust
        self.thirst = thirst

MrBob = Pet("MrBob", 101, 90, 16, 35)
if MrBob.name != MrBob:
    print("Not MrBob")
else:
    print("Is MrBob")
if MrBob.friendliness > 100:
    print("MrBob heppy")
else:
    print("MrBob angy")
if MrBob.hunger > 100:
    print("MrBob Hungy!")
