import random

def loot():

    def save(): #fonction save pour stocker les données de la partie du joueur

        list = [ #liste les données tout en 'str' car elles vont aller dans un .txt
            name,
            str(hp),
            str(atk),
            str(defense),
            str(boostatk),
            str(boostdefense),
            str(xp),
            str(lvl),
            str(heal),
            str(bomb),
            str(rope),
            str(x),
            str(y)
            ]

        f = open('load.txt', 'w') #ouvre un .txt pour y écrire les données ('w' pour 'write')

        for item in list: #ecrit les donnees dans le txt sous forme de liste pour qu'elles soient lisible plus tard
            f.write(item + '\n')
        f.close()

    f = open('load.txt', 'r') #meme systeme de read que dans le fichier charger.py
    load_list = f.readlines()
    name = load_list[0][:-1]
    hp = int(load_list[1][:-1])
    atk = int(load_list[2][:-1])
    defense = int(load_list[3][:-1])
    boostatk = int(load_list[4][:-1])
    boostdefense = int(load_list[5][:-1])
    xp = int(load_list[6][:-1])
    lvl = int(load_list[7][:-1])
    heal = int(load_list[8][:-1])
    bomb = int(load_list[9][:-1])
    rope = int(load_list[10][:-1])
    x = int(load_list[11][:-1])
    y = int(load_list[12][:-1])

    if random.randint(0, 100) <= 60:
        if random.randint(0, 90) <= 30:
            heal += 1
            save()
            print('\nLe combat vous a rapporte 1 Soin !')
            input("\nAppuyez sur ENTREE pour continuer...")
        elif random.randint(0, 90) > 30 and random.randint(0, 90) <= 60:
            boostatk += 1
            save()
            print('\nLe combat vous a rapporte 1 Attaque+ !')
            input("\nAppuyez sur ENTREE pour continuer...")
        elif random.randint(0, 90) > 60 and random.randint(0, 90) <= 100:
            boostdefense += 1
            save()
            print('\nLe combat vous a rapporte 1 Defense+ !')
            input("\nAppuyez sur ENTREE pour continuer...")
    else:
        pass
