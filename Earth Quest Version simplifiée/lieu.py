import ascii
import game
import boss    

def village():
    
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

    if lvl >= 5 and bomb == 0:
        bomb += 1
        save()
        ascii.barre()
        print('             Lieu: Village')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print('Villageois : WOW tu est niveau 5 ? Tiens mon cadeau !')
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nVous gagnez une bombe (elle pourrait servir dans la grotte)')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 1:
        ascii.barre()
        print('             Lieu: Village')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Villageois : J'ai plus de cadeau pour toi desole")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nVillageois : Tu devrais aller voir la grotte au NORD EST du village')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    
    elif bomb == 2:
        ascii.barre()
        print('             Lieu: Village')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Villageois : J'ai plus de cadeau pour toi desole")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nVillageois : Oh mais t'as trouvé une corde dans la grotte !")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nVillagois: Tu veux faire quoi avec ça ? Grimper une tour ? Haha!")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        
    else:
        ascii.barre()
        print('             Lieu: Village')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Villageois : salutations! Euh.. t'as pas l'air très fort pour un aventurier...")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nAu niveau 5.. euh apres un dur entrainement il vous respectera')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    save()
    
def grotte():
    
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
    
    if bomb == 1:
        bomb += 1
        rope += 1
        save()
        ascii.barre()
        print('             Lieu: Grotte')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("L'entree de la grotte est bloquee par un rocher")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nVous lancez la bombe sur le rocher')
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\n*BOOM* L'entree se libere, vous entrez dans la grotte")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 2:
        ascii.barre()
        print('             Lieu: Grotte')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("La grotte s'est effondree, impossible d'y retourner")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nLa corde doit bien servir a quelque chose..')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 0:
        ascii.barre()
        print('             Lieu: Grotte')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("L'entree de la grotte est bloquee par un rocher")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nSi seulement il y avait un moyen de degagez le chemin..')
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nIl y a peut etre des informations au village")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        
def tour():
    
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
    
    if rope == 1:
        ascii.barre()
        print('             Lieu: Tour')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Vous tombez sur une grande tour")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nVous lancez la corde pour escalader jusqu'a l'ouverture" )
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        boss.tour()
    
    elif rope == 2:
        ascii.barre()
        print('             Lieu: Tour')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Vous tombez sur une grande tour")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nLa tour s'est effondree apres votre combat")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nI'l n'y a plus rien a faire dans ce monde")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    
    else:
        ascii.barre()
        print('             Lieu: Tour')
        ascii.barre()
        print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
        print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
        print('Soin:', heal, 'Boost ATK:', boostatk, 'Boost DEF:', boostdefense)
        print('x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Vous tombez sur une grande tour")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nImpossible de rentrer mais vous remarquez une ouverture en hauteur')
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nIl y a surement un moyen de l'atteindre")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    
