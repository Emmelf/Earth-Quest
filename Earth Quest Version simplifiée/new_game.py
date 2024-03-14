import ascii
import game

hp = 30
atk = 5
defense = 4
boostatk = 1
boostdefense = 1
xp = 0
lvl = 1
heal = 2
bomb = 0
rope = 0
x = 0
y = 0

def new_game():
    
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
        
        f = open('load.txt', 'w') #ouvre un .txt pour y écrire les données ('w' pour write)
        
        for item in list: #ecrit les donnees dans le txt sous forme de liste pour qu'elles soient lisible plus tard
            f.write(item + '\n')
        f.close()
    
    ascii.clear()
    ascii.barre()
    print('          Bienvenue sur le RPG')
    ascii.barre()
    print('')
    print(" Tu dois battre le boss pour gagner !\n")
    print('')
    ascii.barre()
    name = str(input('\nCommence par donner ton nom : '))#demander de choisir une nom
    save() #sauvegarde automatique grace a la fonction save
    ascii.clear()
    ascii.barre()
    print('          Bienvenue', name)
    ascii.barre()
    print('')
    print("       La partie est sauvegardee\n")
    print('')
    ascii.barre()
    input("\nAppuyez sur ENTREE pour continuer...")
    game.game()