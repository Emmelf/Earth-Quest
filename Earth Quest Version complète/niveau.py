import ascii
from colorama import Fore
import ascii

def lvlup():

    def screen():
            ascii.barre()
            print(Fore.YELLOW + "🐷 Maitre Cochon :'Bien joué mon poussin ! Tu es au niveau supérieur ! '")
            ascii.niv()
            input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
            ascii.barre()
            print('')
            print('      Tu passes au niveau', lvl)
            print('')
            print('     PV', hp ,'Attaque',atk)
            ascii.barre()

            input("\nAppuyez sur ENTREE pour continuer...")
            ascii.clear()

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

    if xp >= 300 and lvl < 2:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 600 and lvl < 3:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 1000 and lvl < 4:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 1500 and lvl < 5:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 2000 and lvl < 6:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 2500 and lvl < 7:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 3000 and lvl < 8:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 4500 and lvl < 9:
        hp += 1
        atk += 2
        lvl +=1
        save()
        screen()
    elif xp >= 6000 and lvl < 10:
        hp += 1
        atk += 2
        lvl +=1
        save()
    else:
        pass















































