import ascii
import game

def charger(): #la fonction charger attribue la valeur des données depuis le fichier load.txt de sauvegarde
    ascii.clear()
    f = open('load.txt', 'r') #ici on utilise r pour 'read' le fichier load.txt
    load_list = f.readlines() #on va charger la liste et attribuer les bonne valeurs par colone
    name = load_list[0][:-1] #le [: -1] sert a retirer le dernier caractère de la colone pour tout afficher sur une seule ligne
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
    y = int(load_list[12][:-1]) #on pense a typer les donnees correctement au moment de la lecture pour ne pas crash
    
    if hp > 0:
        ascii.barre()
        print('           Sauvegarde trouvee !')
        ascii.barre()
        print('Nom:', name)
        print('Niveau:', lvl)
        print('PV:', hp)
        print('Attaque:', atk)
        ascii.barre()
        
        input("\nAppuyez sur ENTREE pour continuer...")
        game.game()
        
    else:
        ascii.barre()
        print('       Votre personnage est mort !')
        ascii.barre()
        print('Nom:', name)
        print('Niveau:', lvl)
        print('Retour au menu principal')
        print('')
        ascii.barre()
        
        input("\nAppuyez sur ENTREE pour continuer...")


def load():
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