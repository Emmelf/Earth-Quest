import ascii
import game
import boss
from colorama import Fore

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
        ascii.lvl()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Regarde c'est le village des Dragons ! C'est le seul village qui n'a jamais subi une intervention de l'Homme ! Il faut que t'ailles le voir.'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Euh mon ami cochon... Qui donc suis-je censé aller voir si il n'y a pas d'humain ici?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Le chef des Dragons bien sur ! Quelle question ! Mais ne t'inquiètes pas !")
        print("                   Aussi longtemps que je m'en souviennes, les Dragons ont toujours eu de l'affection pour les humains... Je n'ai jamais compris pourquoi...")
        print("                   Ah tiens, il arrive !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print("Dragon :'Humain... Après avoir tant détruit Dyflo, tu cherches un moyen de récupérer la pierre d'Hope pour t'enfuir avec ton peuple... !")
        print("         Ceci dit, je ne peux t'en vouloir, nous pouvons simplement nous envoler !")
        print("         J'ai quelque chose pour toi car le temps joue contre toi. Tiens voici une bombe fabriqué avec du feu de Dragon, elle te permettra de casser l'entrée de la grotte pour y rentrer.'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nVous gagnez une bombe (elle pourrait servir dans la grotte)')
        print(Fore.YELLOW + "🐷 Maitre Cochon : 'Génial mon petit cochon, reprenons la route! ")
        input(Fore.CYAN +"\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Euh oui...'(Je n'ai pas parler devant le dragon tellement j'ai eu peur, commment je vais faire pour la suite...)")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 1:
        ascii.barre()
        ascii.lvl()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print("Dragon :'Je sais que depuis la nuit des temps, les Dragons et les Hommes s'entendent bien mais t'abuserais pas un peu ?")
        print("         Je viens de te donner la bombe avec le'Fire Grey''")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Ouaa, c'est la première fois que je vois un humain se prendre un vent par un dragon !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,": '...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nVillageois : Tu devrais aller voir la grotte au NORD EST du village')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()

    elif bomb == 2:
        ascii.barre()
        ascii.lvl()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        input("\nAppuyez sur ENTREE pour continuer...")
        print("Dragon :'Je sais que depuis la nuit des temps, les Dragons et les Hommes s'entendent bien mais t'abuserais pas un peu ?")
        print("         Je viens de te donner la bombe avec le'Fire Grey''")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Je vous prie de me pardonner, grand Dragon !")
        print(name,";'Mais que dois-je faire pour..'")
        print("\nDragon :'Il faut t'en servir petit malin !")
        print("         : Tu te demandes ce que tu peux faire avec une corde ? Haha! Alors humain réfléchis, à quoi peut bien te servir ta corde ? Nous autres Dragons avons des ailes...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()

    else:
        ascii.barre()
        ascii.lvl()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Regarde c'est le village des Dragons ! C'est le seul village qui n'a jamais subi une intervention de l'Homme ! Il faut que t'ailles le voir.'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Euh mon ami cochon... Qui donc suis-je censé aller voir si il n'y a pas d'humain ici?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Le chef des Dragons bien sur ! Quelle question ! Mais ne t'inquiètes pas !")
        print("                   Aussi longtemps que je m'en souviennes, les Dragons ont toujours eu de l'affection pour les humains... Je n'ai jamais compris pourquoi...")
        print("                   Ah tiens, il arrive !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print("Dragon :'Humain... Après avoir tant détruit Dyflo, tu cherches un moyen de récupérer la pierre d'Hope pour t'enfuir avec ton peuple... !")
        print("         Ceci dit, je ne peux t'en vouloir, nous pouvons simplement nous envoler !")
        print("         Ceci dit, j'ai rarement vu un faible comme toi, ta seule présence parmi nous, est une offense... Tu n'as rien à faire ici... Disparais !")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Grand Dragon j'ai beoin de votre aide pour...'")
        print("Dragon :'Comment oses-tu rester ici ? Dégage !'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Ouaa, c'est la première fois que je vois un humain se prendre un vent par un dragon !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon : 'Je suppose que t'es vraiment spécial HAHAHAHA ! Un faible spécial ! '")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print('\n Partez et revenez quand vous serez au niveau 5.. euh il vous respectera un peu plus... En tout cas je vous le souhaite !  ')
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
        ascii.corde()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon:'L'entree de la grotte est bloquee par un rocher !  Mais oui, il faut se servir de la bombe avec le 'Fire Grey' !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":' C'est quoi le 'Fire Grey' ?' ")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'On ne vous apprend rien à l'école  ou quoi ? Le 'Fire Grey' est le feu de Dragon, bien sur ! ")
        print("                     Et j'ajouterais que c'est la forme d'énergie la plus puissante sur cette terre !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":' Mais si on lance cette bombe avec ce feu de Dragon, on ne va pas etre pris dans l'exposion ?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Ne t'inquiètes pas il a surement doser pour l'entrée de la grotte... Au cas attend que j'ailles me mettre à l'abri ! '")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print('\nVous lancez la bombe sur le rocher')
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\n*BOOM*")
        print("L'entree se libere, vous entrez dans la grotte")
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 2:
        ascii.barre()
        ascii.corde()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'On revient sur nos pas ! Il faut qu'on avance ...'")
        print("                   Il faut utiliser le feu de Dragon donc la bombe!!")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Tiens voila une corde !")
        input("\nAppuyez sur ENTREE pour continuer...")
        print('\nLa corde doit bien servir a quelque chose..')
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
    elif bomb == 0:
        ascii.barre()
        ascii.corde()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon:'L'entree de la grotte est bloquee par un rocher... Comment peut-on passer ?'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":' Alors la, pas la moindre idée, je suis paumée, c'est vous le cochon immortel !' ")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Hélas mon cher ami, il m'arrive d'oublier des choses !' ")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'J'AI TROUVE !!! Il n'a y a qu'un seul moyen !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'Comment on doit faire du coup ?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "\n🐷 Maitre Cochon:'Il n'y a donc qu'un seul moyen de parvenir à l'intérieur de cette grotte....'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":'De quoi tu parles ?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "\n🐷 Maitre Cochon:'Il faut se rendre au village des Dragons et leur demander une bombe fabriquée à partir de 'Fire Grey''")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
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
        ascii.duel()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Regarde-moi cette Tour mon petit... C'est bien la plus grande Tour de cette planète...'")
        print("                   J'imagine sans difficulté que la pierre d'Hope en haut a du stocker stocker une grande quantité d'énergie !")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,": 'Personne n'est jamais arrivé jusqu'ici depuis le temps que mon royaume convoite cette pierre...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Personne n'a jamais eu mon aide aussi junior !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":' Je ne suis pas votre junior ! '")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nVous lancez la corde pour escalader jusqu'a l'ouverture" )
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        boss.tour()

    elif rope == 2:
        ascii.barre()
        ascii.duel()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Regarde-moi cette Tour mon petit... C'est bien la plus grande Tour de cette planète...'")
        print("                   J'imagine sans difficulté que la pierre d'Hope en haut a du stocker une grande quantité d'énergie !")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,": 'Personne n'est jamais arrivé jusqu'ici depuis le temps que mon royaume convoite cette pierre...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Personne n'a jamais eu mon aide aussi junior !'")
        input(Fore.CYAN +"\nAppuyez sur ENTREE pour continuer...")
        print(name,":' Je ne suis pas votre junior ! '")
        input("\nAppuyez sur ENTREE pour continuer...")
        print("\nLa tour s'est effondrée apres votre combat")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "\n 🐷 Maitre Cochon :'Nous somme tous perdus...'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()

    else:
        ascii.barre()
        ascii.duel()
        ascii.barre()
        print('              [☻ Pseudo:', name, ' 🚶‍♂️ Niveau:', lvl,']')
        print('              [♥ PV: ', hp,']', ' [ 🗡️ Attaque:', atk,']', ' [ 🛡️ Defense:',defense,']')
        print('              [🧪 Soin:', heal,'], [ ⚡ Boost ATK:', boostatk,'], [ 🧱 Boost DEF:', boostdefense,']')
        print('              x', x, 'y', y, bomb, rope) #affiche dans quel endroit on se trouve
        ascii.barre()
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Regarde-moi cette Tour mon petit... C'est bien la plus grande Tour de cette planète...'")
        print("                   J'imagine sans difficulté que la pierre d'Hope en haut a du stocker une grande quantité d'énergie !")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,": 'Personne n'est jamais arrivé jusqu'ici depuis le temps que mon royaume convoite cette pierre...'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "🐷 Maitre Cochon :'Personne n'a jamais eu mon aide aussi junior !'")
        input(Fore.CYAN + "\nAppuyez sur ENTREE pour continuer...")
        print(name,":' Je ne suis pas votre junior ! '")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "\n 🐷 Maitre Cochon :'Impossible de rentrer mais regarde il y a une ouverture en hauteur'")
        input(Fore.CYAN +"\nAppuyez sur ENTREE pour continuer...")
        print(name,": 'Mais comment?'")
        input("\nAppuyez sur ENTREE pour continuer...")
        print(Fore.YELLOW + "\n 🐷 Maitre Cochon :'Il y a surement un moyen de l'atteindre'")
        input(Fore.CYAN +"\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
