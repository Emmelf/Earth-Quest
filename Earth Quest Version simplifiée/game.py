import ascii
import random
import charger
import lieu
global play
import niveau
import drop

def game():
    
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
    
    play = True 
    ascii.clear()
    
    #on cree la map grace a une liste qui contien des sous liste pour avoir l'emplacement du joueur en fonction des coordonnees
    
            # x=0       x=1       x=2       x=3       x=4       x=5       x=6   
    map = [['plaine', 'plaine', 'plaine', 'plaine',  'plaine',   'plaine', 'plaine',], #y=0
           ['foret', 'foret',    'foret', 'plaine',  'plaine',    'grotte', 'plaine',], #y=1
           ['foret', 'village', 'foret', 'montagne', 'montagne', 'montagne','plaine'], #y=2
           ['foret', 'foret',   'foret', 'montagne',   'tour',   'montagne', 'plaine'], #y=3
           ['foret', 'foret',   'foret', 'montagne', 'montagne', 'montagne', 'plaine']] #y=4
    
    x_len = len(map[0])-1 # [0] = longeur des sous listes
    y_len = len(map)-1 #-1 pour que la valeur n'attein pas 5 (erreur d'index)
    
    biome = { #on attribue un nom 't' et si un ennemi peut apparaitre 'e' dans chaque case de la map
        'plaine': {
            't': 'Plaines',
            'e': True},
        'foret': {
            't': 'Foret',
            'e': True},
        'montagne': {
            't': 'Montagnes',
            'e': True},
        'village': {
            't': 'Village',
            'e': False},
        'grotte': {
            't': 'Grotte',
            'e': False},
        'tour': {
            't': 'Tour',
            'e': False}
    }
    
    liste_ennemi = ['buisson','arbre','rocher'] #liste des différents ennemis 
    
    ennemi = { #bibliothèque des ennemis pour leur attribuer des stats
        'buisson':{
            'HPM': 20,
            'ATKM': 5,
            'XPM': 300,
        },
        'arbre':{
            'HPM': 30,
            'ATKM': 10,
            'XPM': 600,
        },
        'rocher':{
            'HPM': 40,
            'ATKM': 15,
            'XPM': 1200,
        }
    }
    
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
    
    hpmax = hp
    aggro = False
    passif = True
    
    def combat():
        
        def savecombat():
            
            list = [ #fonction savecombat ajouté sur le tas pour régler le problème des stat qui revenaient a zero quand on gagnait un fight (l'xp par exemple)
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
        
        aggro = True
        
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
        
        if biome[map[y][x]]['t'] == 'Plaines': #3 if pour déterminer quel monstre apparait selon la zone
            zone = 0
        if biome[map[y][x]]['t'] == 'Foret':
            zone = 1
        if biome[map[y][x]]['t'] == 'Montagnes':
            zone = 2
        
        adversaire = liste_ennemi[zone]
        HPM = ennemi[adversaire]['HPM']
        HPMAXM = HPM
        ATKM = ennemi[adversaire]['ATKM']
        XPM = ennemi[adversaire]['XPM']
        hpmax = hp
        
        ascii.barre()
        print('           ATTENTION!')
        ascii.barre()
        print('')
        print('     Un', adversaire, 'vous attaque!')
        print('')
        print('')
        ascii.barre()
        
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        
        while aggro == True:
            
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
            
            ascii.clear()
            ascii.barre()
            print('En combat contre:', adversaire,' / ','Lieu:', biome[map[y][x]]['t'])
            ascii.barre()
            print(adversaire, 'PV:', str(HPM),'/',str(HPMAXM))
            print(name, 'PV:', hp,'/',hpmax)
            print('Soin', str(heal))
            print('Attaque+', str(boostatk),'Defense+', str(boostdefense)) 
            ascii.barre()
            print('[1]-Attaque')
            print('[2]-Soin (20 PV)')
            print('[3]-Attaque+')
            print('[4]-Defense+')
            ascii.barre()
            
            try:
                action = int(input('\nQue faire ? '))
                
                if action == 1:
                    HPM -= atk
                    print('')
                    print('',name, 'attaque', adversaire, 'de', atk,' degats.','\n')
                    input("Appuyez sur ENTREE pour continuer...\n")
                    if HPM > 0:
                        hp -= ATKM
                        print('',adversaire, 'attaque en retour', name, 'de', ATKM,' degats.','\n')
                        savecombat()
                        input("Appuyez sur ENTREE pour continuer...")
                elif action == 2:
                    if hp == hpmax:
                        print('\nVos pv sont deja au maximum !')
                        input("\nAppuyez sur ENTREE pour continuer...")
                    elif hp + 20 < hpmax and heal > 0:
                        hp += 20
                        heal -= 1
                        print('\nLa potion vous soigne de 20pv')
                        input("\nAppuyez sur ENTREE pour continuer...")
                        savecombat()
                    elif heal > 0:
                        hp = hpmax
                        heal -= 1
                        print('\nLa potion vous soigne de 20pv')
                        input("\nAppuyez sur ENTREE pour continuer...")
                        savecombat()
                    else:
                        print("\nVous n'avez pas de soin")
                        input("\nAppuyez sur ENTREE pour continuer...")
                elif action == 3:
                    if boostatk > 0:
                        boostatk -= 1
                        print('\nVous lancez une attaque surpuissante')
                        input("\nAppuyez sur ENTREE pour continuer...\n")
                        HPM -= atk * 2
                        print('',name, 'explose', adversaire, 'de', atk * 2,' degats!','\n')
                        input("Appuyez sur ENTREE pour continuer...\n")
                        savecombat()
                        if HPM > 0:
                            hp -= ATKM
                            print('',adversaire, 'attaque en retour', name, 'de', ATKM,' degats.','\n')
                            savecombat()
                            input("Appuyez sur ENTREE pour continuer...")
                        savecombat()
                    else:
                        print("\nVous n'avez pas d'attaque puissante disponible")
                        input("\nAppuyez sur ENTREE pour continuer...")
                elif action == 4:
                    if boostdefense > 0:
                        boostdefense -= 1
                        HPM -= atk
                        print('\nVous vous renforcez votre corps')
                        input("\nAppuyez sur ENTREE pour continuer...\n")
                        print('',name, 'attaque', adversaire, 'de', atk,' degats.')
                        input("\nAppuyez sur ENTREE pour continuer...\n")
                        if HPM > 0:
                            print('',adversaire, 'attaque en retour', name, "mais ça n'a aucun effet!\n")
                            savecombat()
                            input("Appuyez sur ENTREE pour continuer...")
                    else:
                        print("\nVous n'avez plus de moyen de vous proteger")
                        input("\nAppuyez sur ENTREE pour continuer...")
                ascii.clear()

            except ValueError: #try, exept, pass pour empêcher de crash le jeu si un joueur entre une mauvaise valeur
                ascii.clear()
                pass 
            if hp <= 0:
                ascii.barre()
                print('           GAME OVER!')
                ascii.barre()
                print('')
                print('     Vous etes mort !')
                print('')
                print('     Retour menu principal')
                ascii.barre()
                
                input("\nAppuyez sur ENTREE pour continuer...")
                ascii.clear()
                quit()
            elif HPM <= 0:
                xp += XPM
                hp = hpmax
                savecombat()
                ascii.barre()
                print('           VICTOIRE !')
                ascii.barre()
                print('')
                print('     Vous avez battu', adversaire)
                print('')
                print('     Fin du combat. ','+',XPM,'XP')
                ascii.barre()
                
                input("\nAppuyez sur ENTREE pour continuer...")
                drop.loot()
                ascii.clear()
                niveau.lvlup()
                aggro = False
                
    while play == True: #boucle pour s'assurer qu'on retourne au menu seulement avec un play = false dans le code       

     if not passif: #variable passif pour éviter d'entrer en combat dès le début du jeu 
         if biome[map[y][x]]['e']:
             if random.randint(0, 100) <= 30: #fonction random integer pour donner un 'pourcentage' de chance de tomber sur un ennemi
                 aggro = True
                 combat()
     
     if biome[map[y][x]]['t'] == 'Village': #systeme d'evenement en fonction du lieu et de la progression du joueur
        lieu.village() 
    
     if biome[map[y][x]]['t'] == 'Grotte':
        lieu.grotte() 
    
     if biome[map[y][x]]['t'] == 'Tour':
       lieu.tour()
    
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
            
     ascii.barre()
     print('             Lieu:', biome[map[y][x]]['t']) #affiche le lieu en fonction des "coordonnees" du tableau map
     ascii.barre()
     print('Pseudo:', name, '[Niveau:', lvl,']', 'xp', xp)
     print('[PV:', hp,']', '[Attaque:', atk,']', '[Defense', defense,']',)
     print('[Soin:', heal,']', '[Boost ATK:', boostatk,']', '[Boost DEF:', boostdefense,']')
     print('Position : [x', x,']', '[y', y,']') #affiche dans quel endroit on se trouve
     ascii.barre()

     print('[0]-Sauvegarder et quitter') #jeu avec des if pour afficher seulement les directions possibles
     if y > 0:
         print('[1]-Aller vers le NORD')
     if y < y_len:
         print('[2]-Aller vers le SUD')
     if x < x_len:
         print("[3]-Aller vers l'EST")
     if x > 0:
         print("[4]-Aller vers l'OUEST")
     ascii.barre()
     
     try:
         destination = int(input('\nQue faire ? '))
         ascii.clear()
     except ValueError: #try, exept, pass pour empêcher de crash le jeu si un joueur entre une mauvaise valeur
         ascii.clear()
         pass 
     
     if destination == 0: #if elif pour que le joueur reste dans la map exemple : si il est tout en haut (y = 0) il ne pourra pas aller plus loin et restera sur place 
        save()
        play = False
     elif destination == 1:
         if y > 0:
             y -= 1
             save()
             passif = False
     elif destination == 2:
         if y < y_len:
             y += 1
             save()
             passif = False
     elif destination == 3:
         if x < x_len:
             x += 1
             save()
             passif = False
     elif destination == 4:
         if x > 0:
             x -= 1
             save()
             passif = False
     else:
         pass
         