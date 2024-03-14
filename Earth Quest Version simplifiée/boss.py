import ascii

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
    
    boss = 'Gardien de la tour'
    hpboss = 100
    hpmaxboss = hpboss
    atkboss = 30
    xpboss = 2000
    aggro = True
    hpmax = hp
    
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
        print('En combat contre:', boss,' / ','Lieu: Sommet de la tour')
        ascii.barre()
        print(boss, 'PV:', str(hpboss),'/',str(hpmaxboss))
        print(name, 'PV:', hp,'/',hpmax)
        print('Soin', str(heal))
        print('Attaque+', str(boostatk)) 
        ascii.barre()
        print('[1]-Attaque')
        print('[2]-Soin (20 PV)')
        print('[3]-Attaque+')
        print('[4]-Defense+')
        ascii.barre()
        
        try:
            action = int(input('\nQue faire ? '))
            
            if action == 1:
                hpboss -= atk
                print('')
                print('',name, 'attaque', boss, 'de', atk,' degats.','\n')
                if hp > 0:
                    hp -= atkboss
                    input("Appuyez sur ENTREE pour continuer...")
                    print('')
                    print('',boss, 'attaque en retour', name, 'de', atkboss,' degats.','\n')
                    save()
                    input("Appuyez sur ENTREE pour continuer...")
            elif action == 2:
                if hp + 20 < hpmax and heal > 0:
                    hp += 20
                    heal -= 1
                    print('\nLa potion vous soigne de 20pv')
                    input("\nAppuyez sur ENTREE pour continuer...")
                    save()
                if heal > 0:
                    hp = hpmax
                    heal -= 1
                    print('\nLa potion vous soigne de 20pv')
                    input("\nAppuyez sur ENTREE pour continuer...")
                    save()
                else:
                    print("\nVous n'avez pas de soin")
                    input("\nAppuyez sur ENTREE pour continuer...")
           
            elif action == 3:
                if boostatk > 0:
                    boostatk -= 1
                    print('\nVous lancez une attaque surpuissante')
                    input("\nAppuyez sur ENTREE pour continuer...\n")
                    hpboss -= atk * 2
                    print('',name, 'explose', boss, 'de', atk * 2,' degats!','\n')
                    input("Appuyez sur ENTREE pour continuer...\n")
                    save()
                if hpboss > 0:
                    hp -= atkboss
                    print('',boss, 'attaque en retour', name, 'de', atkboss,' degats.','\n')
                    save()
                    input("Appuyez sur ENTREE pour continuer...")
                    save()
                else:
                    print("\nVous n'avez pas d'attaque puissante disponible")
                    input("\nAppuyez sur ENTREE pour continuer...")
                        
            elif action == 4:
                if boostdefense > 0:
                    boostdefense -= 1
                    hpboss -= atk
                    print('\nVous vous renforcez votre corps')
                    input("\nAppuyez sur ENTREE pour continuer...\n")
                    print('',name, 'attaque', boss, 'de', atk,' degats.')
                    input("\nAppuyez sur ENTREE pour continuer...\n")
                    if hpboss > 0:
                        print('',boss, 'attaque en retour', name, "mais ça n'a aucun effet!\n")
                        save()
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
        elif hpboss <= 0:
            xp += xpboss
            hp = hpmax
            rope += 1
            save()
            ascii.barre()
            print('           VICTOIRE !')
            ascii.barre()
            print('')
            print('     Vous avez battu', boss)
            print('')
            print("     Le jeu est termine, merci d'avoir joue")
            ascii.barre()
            
            input("\nAppuyez sur ENTREE pour continuer...")
            ascii.clear()
            aggro = False
            quit()