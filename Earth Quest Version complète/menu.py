import new_game 
import charger
import credits
import ascii #la fonction pour embellir le jeu avec plein d'ascii stockes
from colorama import Fore

def menu(): #creation de la fonction du menu dans le fichier menu
    
  ascii.titre()
  ascii.clear()
  print(Fore.BLUE + '                                         Menu principal')
  ascii.barre()
  print(Fore.BLUE +'                                         [1]-Nouvelle partie')
  print(Fore.BLUE +'                                         [2]-Charger partie')
  print(Fore.BLUE +'                                         [3]-Credits')
  print(Fore.BLUE +'                                         [4]-Quitter')
  ascii.barre()

ascii.clear()
menu()#appel a la fonction du menu
choix = int(input('\nChoisissez une option : '))#demander de choisir une option

while choix != 4: #boucle pour faire tourner le menu tant qu'on ne choisi pas de quitter (option 4)
    if choix == 1:
        new_game.new_game()
        ascii.clear()
    
    elif choix == 2:
        try: #lire le .txt de sauvegarde, vérifier qu'il y a bien toute les donnees sinon dire que la save est corrompue
            f = open('load.txt', 'r') #on peut voir que ça fonctionne si on supprime des lignes dans le .txt
            load_list = f.readlines()
            if len(load_list) == 13: 
                charger.charger()
                ascii.clear()
                
            else:
                ascii.clear()
                ascii.barre()
                print('                 ERREUR')
                ascii.barre()
                print('')
                print("          Sauvegarde corrompue !\n")
                print('')
                ascii.barre()
                input("\nAppuyez sur ENTREE pour continuer...")
                ascii.clear()
                
        except OSError: #exception si erreur sur la cmd dire qu'il n'y a pas de sauvegarde
            ascii.clear()
            ascii.barre()
            print('                 ERREUR')
            ascii.barre()
            print('')
            print(" Il n'y a pas de sauvegarde disponible !\n")
            print('')
            ascii.barre()
            input("\nAppuyez sur ENTREE pour continuer...")
            ascii.clear()
            
    elif choix == 3:
        credits.credits()
        ascii.clear()
    
    else:
        ascii.clear()
        ascii.barre()
        print('                 ERREUR')
        ascii.barre()
        print('')
        print("   Choisissez une option entre 1 et 4\n")
        print('')
        ascii.barre()
        input("\nAppuyez sur ENTREE pour continuer...")
        ascii.clear()
        
    menu()#appel a la fonction du menu a nouveau
    choix = int(input('\nChoisissez une option : '))#demander de choisir une option a nouveau

print('au revoir')
