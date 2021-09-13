import random
ronde = 1
i = 0
score = 0
while ronde < 20:
    doorgaan = input("Wil je door gaan?")
    if doorgaan == "ja":
        random = random.randint(0, 1000)
        while i < 10:
            gok = int(input("gok een getal \n"))
            if gok > 1000:
                break
            if gok == random:
                print("Je hebt gewonnen!")
                score += 1
                break
            else:
                if gok > random:
                    print("Lager")
                    if gok - random < 50 and gok - random > 20:
                        print("Je bent warm")
                    elif gok - random < 20 and gok - random > 0:
                        print("Je bent heel warm")
                else:
                    print("Hoger")
                    if random - gok < 50 and random - gok > 20:
                        print("Je bent warm")
                    elif random - gok < 20 and random - gok > 0 :
                        print("Je bent heel warm")
            i += 1
            score += 0
    else:
        break
        ronde += 1
