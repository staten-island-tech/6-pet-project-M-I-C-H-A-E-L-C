import random
class Pet:
    def __init__(self, name, friendliness, hunger, anger, thirst, weight):
        self.name = name
        self.frnd = friendliness
        self.hngr = hunger
        self.angr = anger
        self.thrs = thirst
        self.lbs = weight
MrBob = Pet('MrBob', 1, 1, 1, 1, 1)
MrBob.frnd = random.randint(1,100) # Friendliness
MrBob.hngr = random.randint(1,100) # Hunger
MrBob.angr = random.randint(1,100) # Bloodlust
MrBob.thrs = random.randint(1,100) # Thirst
MrBob.lbs = random.randint(10,100) # Weight
print("MrBob")
print("😄", MrBob.frnd, "🍖", MrBob.hngr, "🤬", MrBob.angr , "💧", MrBob.thrs)
while MrBob.hngr >= 1 and MrBob.thrs >= 1:
    if MrBob.hngr <= 15:
        print("MrBob in critical hunger levels! Consider feeding")
    if MrBob.thrs <= 15:
        print("MrBob in critical thirst levels! Consider giving water")
    print("Command")
    print("Play")
    print("Feed")
    print("Give Water")
    print("Ignore")
    comm = input(": ").upper()
    if comm != "PLAY" and comm != "FEED" and comm != "GIVE WATER" and comm != "IGNORE":
        print("Play, Feed, Give water or Ignore you chud")
        comm = input(": ").upper()
    if comm == "PLAY":
        if MrBob.hngr <= 30 or MrBob.thrs <= 30:
            MrBob.frnd -= random.randint(1,10)
            print("😰 MrBob no want to play anymore")
        else:
            MrBob.frnd += random.randint(1,10)
        MrBob.hngr -= random.randint(1,10)
        MrBob.angr -= random.randint(1,10)
        MrBob.thrs -= random.randint(1,10)
        MrBob.lbs -= random.randint (1,10)
        print("🫃🔻", MrBob.lbs, "😄🔺", MrBob.frnd, "🍖🔻", MrBob.hngr, "🤬🔻", MrBob.angr , "💧🔻", MrBob.thrs)
    elif comm == "FEED":
        MrBob.frnd += random.randint(1,10)
        MrBob.hngr += random.randint(1,10)
        MrBob.angr -= random.randint(1,10)
        MrBob.thrs -= random.randint(1,10)
        MrBob.lbs += random.randint (1,10)
        print("🫃🔺", MrBob.lbs, "😄🔺", MrBob.frnd, "🍖🔺", MrBob.hngr, "🤬🔻", MrBob.angr , "💧🔻", MrBob.thrs)
    elif comm == "GIVE WATER":
        MrBob.frnd += random.randint(1,10)
        MrBob.hngr -= random.randint(1, 5)
        MrBob.angr -= random.randint(1,10)
        MrBob.thrs += random.randint(5,20)
        print("😄🔺", MrBob.frnd, "🍖", MrBob.hngr, "🤬🔻", MrBob.angr , "💧🔺", MrBob.thrs)
    elif comm == "IGNORE":
        MrBob.frnd -= random.randint(1, 10)
        MrBob.hngr -= random.randint(1, 10)
        MrBob.angr += random.randint(20,50)
        MrBob.thrs -= random.randint(1, 10)
        print("😄🔻", MrBob.frnd, "🍖🔻", MrBob.hngr, "🤬🔺", MrBob.angr , "💧🔻", MrBob.thrs)
    if MrBob.angr >= 100:
        print("MR BOB SINISTER WE'RE DOOMEDDDD")
        break
    elif MrBob.lbs >= 200:
        print("MrBob passed away from 'not' hungry")
        break
    elif MrBob.lbs >= 100:
        print("MR BOB OBESE! MAYBE PLAY A LITTLE")
if MrBob.hngr <= 1 or MrBob.thrs <= 1:
    print("MrBob passed away from your negligence. Next time, watch him responsibly.")
    print("⠐⠢⢒⠐⡢⠒⢔⠈⣿⡹⣏⢿⣝⢯⣟⡽⣯⡻⣯⣻⡻⣻⡻⣻⣻⢟⣿⣻⣟⣿⣻⣟⡿⡿⡿⣿⢿⢿⡿⣿⢿⡿⠿⠿⠧⠢⡱⢌⠮⡰⡑⡌⢆⠕⡌⠦⡱⡨⢢⢊⢆⠕⡌⢆⢕⠌⡆⢕⠜⡰⡁⢎⠦⡱⡨⣉⣵⣵⣿⣿⢿⡿⣿⢿⡿⣿⢿⡿⡿⡿⡿⣿⢟⣿⣟⣿⢟⣿⣻⣟⢿⣻⣻⡻⣻⣻⣝⢿⣝⢯⣟⡽⣯⡻⣝⡯⣻⢝⡯⣻")
    print("⠈⡅⡱⢈⠔⡑⢌⠢⢸⣝⣝⢷⣹⡳⣝⢾⡵⡻⣮⣳⡽⣫⣟⣽⡳⡿⣵⢯⣞⡷⣽⣞⢿⡽⣟⣽⣻⢯⡿⣝⣓⢚⢛⠪⡊⢕⢊⠆⢕⢌⠢⡱⡈⢎⡘⢔⢌⢢⠱⡨⢢⢑⠜⡰⣁⠎⢜⡐⢕⢌⠪⡘⠔⠕⡔⢔⡈⠻⠞⣯⣻⣟⣽⢯⡿⣾⣫⡿⣽⣻⡽⣯⡻⡷⣽⢞⣟⢷⢯⡾⣫⡷⣽⣝⢷⡳⣝⢷⣹⡳⣝⢾⡪⣟⢼⣝⢮⡻⣪⣻")
    print("⠐⠌⢄⠅⡊⠔⡠⢃⠄⢷⡹⡳⣵⢫⢯⢞⡽⣹⢮⢮⡻⣺⢮⢾⣹⡻⣺⢯⠞⠟⠮⡋⡛⡘⢍⠥⡉⢎⢌⢌⠢⡡⠡⡃⢪⠂⡕⡘⢔⠡⡑⣌⠸⣠⣷⣾⣾⣷⣿⣷⣿⣿⣿⣾⣶⣵⣥⣘⡄⢎⢌⢊⠪⢊⠔⢥⢘⠡⡋⡩⢚⡑⡛⠟⢞⠷⣻⢞⡷⣻⢞⣽⣝⣟⢾⣫⢯⣻⡳⣽⡫⡾⢮⣞⡭⣯⢫⡗⣽⡪⣯⢺⡝⣮⢳⡕⣯⢺⢕⢷")
    print("⠀⡑⠢⡈⠆⡨⢂⠢⢂⠱⣫⡻⣜⢗⡽⣣⢟⡵⣫⡳⣝⢷⡹⡧⢋⠩⡂⢆⢑⠍⡒⢌⠪⡘⢔⠱⡨⠢⡑⢌⠢⢊⢔⠑⢅⠪⡐⡡⢊⠌⡢⣾⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣥⡕⢡⠊⡔⢁⠇⢌⠢⡑⢌⢌⠪⢢⠑⡌⠻⣝⡽⣫⢾⣪⢗⣯⢳⢯⡞⣽⡪⣏⢟⡵⣣⢟⡼⣣⡻⣪⢞⢵⡫⡺⣕⢝⢮⡣⣏⢗⢽")
    print("⠠⡁⡑⡈⠔⠐⢄⠑⡄⡈⢧⡹⣪⡳⣹⢪⢞⢮⡣⡻⠜⢕⠋⡪⢐⠕⡨⠢⡑⢌⠪⡐⠕⢌⢢⢑⠌⢆⠱⡀⢣⠊⢔⠡⢃⠌⣢⠘⣴⡏⡼⣿⣧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠑⢌⠢⡑⢔⠡⢊⠤⡡⡑⢅⠕⢌⠆⢬⢈⡙⠣⠫⢗⡽⣣⢟⡼⣣⢟⣜⢏⡞⡵⣝⢼⢕⡝⣎⢷⡱⡝⣮⢪⡳⢵⢕⡵⡹⣪")
    print("⠀⠢⢈⠄⡑⢁⠢⢁⠢⡐⠨⣎⠧⠳⠕⡩⠡⡑⠔⡐⡑⢌⠢⢑⠄⡣⠘⢔⠡⡊⢔⠡⡑⢅⠢⡑⢌⠢⡑⢌⠄⢣⢈⢂⠑⢰⡏⣴⣿⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢂⠕⡈⡂⠱⡀⠕⡐⢌⠢⡑⢔⠡⠢⡂⠱⡁⠣⠢⡈⢅⠛⢼⡱⣫⢎⢗⢝⢮⡪⡮⣣⢫⢎⢮⡚⡮⣪⢣⡫⡺⣘⢎⣎⢳")
    print("⢀⠑⠄⠢⠈⠔⠠⡁⠢⢐⠀⡣⢘⠐⢅⠌⢢⠘⢄⠑⠌⠢⡘⠄⡪⠐⡅⠱⡈⢢⠡⡑⢌⠢⡑⢌⠢⠑⢄⠢⠘⢄⠢⠁⠢⣼⡧⣿⣿⣿⠿⠛⡡⢈⠫⢿⣿⣿⣿⣿⣿⣿⣿⢋⡠⣠⢈⠍⠻⢿⣿⣿⣿⣿⣧⠈⠢⡨⢈⠆⢌⠊⢔⠡⢊⠔⠡⡊⠢⡑⢑⠌⡑⡡⠊⠔⡡⠢⡈⠣⣫⢎⢗⠵⣕⠵⣕⢝⡪⡣⣝⢜⢖⢕⡝⣜⢕⡣⣎⢳")
    print("⢀⠌⢂⠡⠑⡈⢐⠀⡑⢀⠕⠐⢄⠃⡢⠘⢄⠑⢌⠊⠜⡐⠈⠢⡈⠢⢊⠌⢢⢁⠪⡐⠡⡊⡐⡡⢊⠌⠢⡈⢊⠄⠄⢁⣾⣿⣿⠿⣉⣡⢖⢷⣙⡝⣧⢛⣿⣿⣿⣿⣿⣿⢏⡽⡝⡵⣫⡻⢶⣦⣬⣙⢿⣿⣿⣧⠐⢄⠡⢂⠑⡄⢅⠪⡐⢅⠱⢈⠂⠜⡠⠑⢌⢄⠩⠢⡈⢆⢘⠐⠌⣣⢫⡚⣜⢎⢮⢪⡪⡳⢜⢬⡣⣓⢕⠮⡪⡪⡲⢕")
    print("⠀⢂⠐⠄⠡⡀⠅⢐⠀⠆⢌⠊⢄⠑⠄⠣⡈⢊⠄⡱⢈⠔⠁⢈⠔⡡⡁⠪⡐⢄⠑⢌⠢⡈⢆⠰⡁⡊⠔⡐⠔⠀⠊⣰⣿⣿⣵⣾⣿⣿⠿⢓⣙⡘⢮⡳⡹⣿⣿⣿⣿⢏⡾⡹⣞⢝⢈⣛⡛⠿⣿⣿⣷⣾⣿⣿⡆⠠⠑⢄⠁⠒⢄⠑⠔⡈⠢⡁⠠⢃⠌⢌⠢⠠⢃⠌⠢⢂⠅⡑⠌⡰⡣⡝⡬⡪⡪⣣⢚⡜⡕⢕⢎⢎⠮⡱⡍⢮⠪⡳")
    print("⠀⢂⠁⠌⡐⠠⠈⢄⠀⡑⢄⠑⢄⠑⡁⡑⠌⢄⢑⠐⢄⠊⡂⠀⠢⠐⢌⠢⡈⠢⡑⢄⠑⠔⢄⠑⢄⠊⠔⠐⠄⢈⠀⣻⣿⣿⣿⡿⣫⣴⣆⣤⣿⣷⡜⢽⡕⣽⣯⢿⣯⣗⣝⣝⢎⣴⣿⣿⣤⣤⣦⣙⢿⣿⣿⣿⡣⠀⡑⠠⡁⢃⠢⠑⡡⢊⠂⠂⠨⡂⢌⠂⡅⠱⠠⡑⠡⠢⠨⡠⠡⠘⠜⠬⠪⡪⢪⢒⢕⢪⠪⡣⡣⡣⡫⡪⡪⡣⢝⢜")
    print("⠐⠠⠈⠄⠐⡈⠐⡀⠂⠌⡠⠊⢄⠡⡈⠔⡈⠢⡐⠡⢂⠅⢌⠀⡈⢊⠐⢄⠅⡑⡐⢌⢈⠊⢄⠣⢈⢊⠨⠂⠂⠄⠠⣏⣿⣿⣏⣴⣿⣿⣿⣿⣿⣿⡟⡺⣸⣿⣯⢶⣿⣿⣮⡮⡃⣿⣿⣿⣿⣿⣿⣿⣶⣼⣿⡿⣌⠀⠐⠠⠊⢄⠅⡑⠔⠠⡑⠈⡂⠢⡈⠢⡈⠢⢑⢈⢂⠑⠔⡠⠑⡈⠐⠠⢁⠠⠂⠠⠁⡁⢉⠈⢊⠘⠌⠪⠜⢜⠌⢧")
    print("⠠⡀⠡⠈⡐⠀⠡⠀⠌⢐⢀⢊⠐⢄⠊⡐⠌⠢⡈⢂⠡⠂⠢⠂⢀⠈⡂⠆⢌⠐⢌⠠⢊⢈⠢⠐⠅⢄⠁⠐⣠⡂⠸⣵⣿⣿⣿⣻⢿⣿⣿⣿⣿⣿⡿⣾⣿⣿⣿⢹⣯⣿⣽⣿⣯⣻⣾⣽⣿⣿⢿⣿⣻⣿⣿⣿⢆⣰⣎⠈⢂⠡⢂⠌⡨⢂⠀⠔⡈⠢⡈⠢⡈⠢⡁⠢⡐⡁⢊⠄⠂⠄⠑⠐⡀⠂⠄⡁⠐⠠⠀⢂⠀⢂⠐⢀⠂⠄⡈⢀")
    print("⠄⢀⠂⠐⢀⠁⡐⠁⠐⡀⠢⡀⡑⠄⡡⢈⠔⢁⠔⢁⠌⢊⠐⢅⠀⠄⢈⠢⢐⠁⠢⡁⠢⢁⠌⡨⠂⢀⠐⠀⢟⣷⢨⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⡿⣘⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢲⡿⣱⡀⠀⡑⠄⡊⠠⠂⢀⠊⢄⢑⠈⡢⢈⠢⡈⠢⠐⠌⡠⠊⣀⢊⠠⠁⢄⠈⠄⠠⠁⠄⠡⠀⢂⠀⢂⠀⠂⠄⠠⠀")
    print("⠠⠀⢄⠁⡄⣂⢤⢨⠔⡤⠂⠔⢐⠐⠄⠢⠐⡁⠔⠠⠊⡠⠑⠠⡂⠠⠀⡑⠄⡑⠡⡐⢁⠢⠂⠀⠄⠀⠄⠈⡮⣙⢇⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣿⣿⣷⡿⣿⣵⣿⣿⣻⣿⣿⣿⣿⡿⣾⣿⣿⣿⣿⣿⣿⣿⡿⡙⣕⢎⡆⠀⠀⢊⠄⠡⠀⢄⠑⠄⠢⡁⠢⢐⠁⠔⡁⡑⢐⠄⣸⢅⢧⢫⢓⡕⣕⢓⢎⡲⡢⢦⢢⢄⢆⢄⣈⡀⠂⠄⡈")
    print("⢞⢸⡨⣃⢗⠜⡦⡣⣫⡘⣇⠨⡀⠡⠊⡐⠡⡐⢈⠢⠁⠔⢁⠢⠂⠂⠀⢐⠈⠔⢠⠈⠄⠠⠀⠂⠐⠀⠄⠈⡾⣨⢣⠺⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣻⣟⣿⣽⣾⣿⣯⣿⣿⣟⣿⣿⣻⣿⣻⣿⣿⣿⣿⣿⡙⣆⢗⠵⠂⠀⠁⠠⡈⢀⠀⡂⠡⠊⡐⢈⠄⡡⢈⠂⠔⢈⠄⠂⡮⣪⢎⢧⢳⡱⡪⣕⠵⡱⡙⡦⡓⡵⡱⡣⡪⡪⡫⡪⢢")
    print("⡪⡲⣑⢎⢎⡳⡱⡕⢮⢪⠮⡄⠄⡑⢈⠐⡐⠄⠡⢐⠁⡊⠄⢂⠡⠑⠀⠀⠌⠢⠠⠁⠐⠀⠐⠀⠂⠀⠂⠀⠫⡜⣕⢹⡹⣿⣿⣿⣿⣿⣻⣿⣯⣿⣷⣿⣿⣿⣿⡿⣿⣿⡷⣿⣿⣻⣿⣿⢿⣟⣿⣿⣿⡟⡵⢪⢎⡕⠏⠀⠀⠂⢀⠀⠀⢄⠨⠂⡡⠈⠔⢀⠆⢄⠑⡨⠠⡈⢜⡵⣱⡣⡳⣕⢕⣝⢜⢎⡳⣙⢜⢎⢞⢜⠮⡪⣎⢎⢎⢕")
    print("⡪⢎⢮⡱⣍⢞⢜⡝⣪⢣⡛⣦⠈⡐⠄⠡⡐⢈⠂⡡⠐⠄⢊⠠⢂⠑⡈⠀⠀⠑⠀⠐⠀⢈⠀⠄⠈⠀⠂⢀⠀⠫⣪⡑⣗⢜⡻⣿⣿⣿⣿⣷⣿⣿⣻⣿⢾⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⡫⢮⠝⡴⡣⠋⠀⠀⠄⠁⠀⠀⠂⠐⠄⡡⠐⡁⢊⠠⢂⠐⠄⠢⠐⢠⢟⢼⡪⣎⢗⡕⡧⣣⢫⢎⢧⢫⡪⣣⢫⡪⡳⡹⣔⢝⡜⣕")
    print("⢪⡳⡱⢎⢮⡪⣣⢝⡜⣕⢝⡬⡣⠀⡊⠐⡠⠁⡂⠔⢈⠄⠡⠂⢄⠡⠐⠀⠁⠀⠁⠀⠂⠀⠀⠄⠀⠁⡀⢀⠀⠀⠑⡵⡩⣎⢗⢭⡻⣾⣿⣾⣿⣟⣿⡿⣿⣿⣿⢔⣿⣿⣿⣾⣿⣿⣾⣿⣿⣾⣏⢎⢗⡝⠪⡓⠁⠀⠐⠀⠐⠀⠁⢀⠈⢈⠐⠄⢌⠐⠄⠢⠠⠡⡈⢂⠁⣾⢱⢗⡵⣣⢏⡞⡼⣱⢫⢎⢗⢵⡱⡕⡵⡱⡹⡪⣎⢞⡜⡮")
    print("⢕⡵⣹⡱⡣⡳⣕⢝⢮⡪⡳⣍⣻⡀⠌⠐⠄⡨⠀⠌⢄⢈⠂⡑⢀⢂⠑⡀⠁⠀⠁⡀⠈⠀⠐⠀⡐⠀⠄⠠⠈⠄⠁⠀⠈⣮⢪⡳⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣷⣿⣿⣯⣿⣿⣿⣿⣙⢮⡩⠀⠀⠐⠀⠂⠐⠀⠐⠀⢀⠀⡀⠀⡁⢂⠌⠐⡡⢈⠂⠔⠈⣰⢗⢽⡕⡽⣜⢵⢝⢮⢳⢕⣏⢳⡕⣝⢮⠺⣕⢝⢮⡪⣣⡫⣺")
    print("⡪⡞⡴⣹⢪⡳⣕⢝⣎⢞⡕⣗⠼⡦⠈⠂⠢⡀⢑⠈⠄⢂⠨⠀⠢⠐⠄⠀⡀⠈⢀⠀⠄⠡⠈⠄⠄⠨⡀⠡⠈⠀⠐⠀⠸⣔⠕⣽⣿⣿⣿⣿⣿⣾⣿⣽⣿⣾⣿⡇⣿⣿⣿⣿⣽⣿⣿⣾⣿⣿⣾⣷⡕⢼⠀⠂⠐⠀⠁⢐⠀⢂⠀⠄⠀⠀⡀⠀⠠⠈⡂⠐⠄⡈⢂⢐⢷⡹⡮⣞⣝⢮⡳⣝⢧⢻⢜⢮⡣⣯⡪⣳⢝⣎⢳⡕⣝⢼⡱⡳")
    print("⢽⢜⣕⢗⢵⠳⣕⢽⡸⣪⡳⣹⡪⣻⡄⠑⠠⠂⠄⠡⠈⠄⢂⠡⠁⠌⠀⠠⠀⠂⠄⢂⠈⠄⠊⢀⠂⡁⢀⠐⠀⠈⢀⠀⢪⣌⢻⣿⣻⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⡇⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⢟⡸⡁⠀⠄⠐⠀⠠⠈⡀⠂⠐⢈⠀⡠⠀⡀⠀⠈⠄⠡⠐⡀⣾⢱⣏⢾⡪⣞⢵⡫⣞⢵⣫⡳⡳⣝⢦⡻⣜⢧⡫⣞⢼⢕⢧⣛⢮")
    print("⣗⢵⡣⣏⡳⣫⢮⡳⣹⢪⢮⣣⢻⡔⡷⠈⠠⠁⠌⢂⠁⠊⠠⠀⠌⡀⢁⠂⠁⠌⡀⠂⡐⠈⡐⠠⠀⠄⠐⠀⠈⠀⠀⡀⢰⢕⢕⣿⢹⣿⣷⣿⣿⣿⣿⣾⣿⣿⣿⡧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⠇⡇⡞⠄⠀⠐⠠⠀⠂⠐⠀⢂⠐⠀⠄⠠⠀⢄⠈⠄⠈⠄⡁⠰⢯⢞⣮⢳⣝⢞⢷⢝⢾⢵⡣⣯⢻⡜⣧⢻⡜⣧⡻⣜⢧⡻⣱⢳⡕")
    print("⣕⢗⡽⣜⢝⡮⣺⢜⢧⡻⡪⡮⡳⣝⢞⡅⠨⢀⠅⠠⠁⠌⠠⢈⠀⡐⠀⠌⠐⠠⠐⠠⠐⠀⠔⠀⠄⡈⠄⠀⠁⠀⠂⠀⢱⡹⡢⢽⣷⢹⣿⡻⣿⡽⣿⣿⣿⣿⣿⡧⣹⣿⣿⣿⣿⣿⣿⣿⣿⠯⡹⡡⡇⣝⠂⠀⡀⠁⠄⠀⡀⠡⠀⠌⢀⠊⢀⠁⡀⠂⡈⠐⡀⠐⡀⠄⠈⢮⡳⣝⣝⢗⡯⣳⢏⡾⣕⢯⡺⣕⢯⡺⡵⣝⢮⡳⣝⡵⡳⣝")
    print("⢪⡗⣵⢝⢮⡺⡕⣯⢪⡗⣽⢪⢯⡪⡯⡽⡄⠂⠄⠑⠀⠂⠁⠄⠐⢀⠁⠐⠁⠄⠡⢀⠁⡈⢀⠂⠠⠀⠄⠀⠁⡀⠐⠀⠀⢧⡙⣼⣿⣿⣿⣷⣻⣿⣿⣿⣟⣿⣿⡗⢼⣿⣿⣿⣿⢧⣿⡏⢗⠭⡪⢪⢊⢮⠁⠀⠀⠐⠠⠀⠀⠀⠂⠐⡀⠐⡀⠐⠀⠌⢀⠐⠀⢂⠀⡐⠀⡀⠀⠱⣝⣝⢾⢵⡫⡾⣕⢯⡞⣵⡫⣞⢗⡽⣕⢯⡺⣎⢟⡼")
    print("⣏⢞⢮⡳⣝⢮⡳⣕⢯⡺⣪⢗⡽⣚⢞⡮⣳⠀⠂⢁⠈⡀⠡⠀⡁⠄⢈⠀⡁⠐⠀⠄⠐⠀⠄⠂⠠⠁⠀⠈⠀⠀⠀⡀⠀⠀⡇⢺⣿⣟⣿⢿⣿⣟⣿⣽⡿⣿⣽⠣⡪⣿⣿⣽⣿⢷⡟⢜⢌⡣⡓⡕⢱⠂⠀⠀⠀⠁⠐⠀⠄⠀⠈⠄⠐⠀⠄⢁⠈⠠⠀⠄⠁⠠⠀⠄⠠⠀⠂⠀⣫⢞⣵⡫⣞⡽⣪⢗⡽⣪⢗⡽⣕⢯⡺⣕⢟⢮⡻⣜")
    print("⢮⣫⢳⡝⣮⢳⡝⣮⢳⣝⢵⣫⢞⡽⣱⢯⡹⡇⠀⠄⠠⠐⠀⠂⠀⠠⠀⠄⠀⢈⠀⠌⢀⠁⠄⠈⠠⠀⡁⠀⠂⠈⠀⠀⠀⠀⢣⢃⢻⣟⣿⣻⡷⣿⢿⣽⣟⡿⣿⢈⢮⣿⢷⣿⣽⣿⢘⠬⡪⣘⢌⢎⢪⠀⠀⡀⠈⠀⠁⠐⠀⠈⠀⠂⢈⠀⠂⡀⠐⠀⠂⡀⢁⠐⠀⠂⠄⢈⠀⠂⢸⢯⣪⢗⡽⣪⢗⡯⣺⢳⣝⢮⡳⣝⡽⣪⢯⡳⣝⢮")