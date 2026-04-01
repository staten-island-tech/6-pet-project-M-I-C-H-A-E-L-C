class Pet:
    def __init__(self, name, friendliness, hunger, bloodlust, thirst):
        self.name = name
        self.friendliness = friendliness
        self.hunger = hunger
        self.bloodlust = bloodlust
        self.thirst = thirst
MrBob = Pet("Mr.Bob", 100, 35, 16, 35)
for i in Pet:
    if MrBob.hunger > 100:
        print("MrBob hangy")