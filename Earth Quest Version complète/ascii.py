import os
import pyfiglet
from colorama import Fore,Style



def barre():
    print('       +---------------------------------------------------------------------------------------------+              ')

def clear(): #fonction qui efface le texte a l'écran pour un aspec esthétique (marche que dans la console)
    os.system('cls')



def titre():
  title = pyfiglet.figlet_format("                       Earth Quest")
  print(Fore.BLUE+title)

def new_game():
  new_game = pyfiglet.figlet_format("                      C'est Parti ! !")
  print(new_game)

def cd():
  credits = pyfiglet.figlet_format("                               Credits")
  print(Fore.CYAN + credits)



def combat():
    monstre = pyfiglet.figlet_format("                         Combat")
    print(Fore.RED +monstre)

def victoire():
    combat = pyfiglet.figlet_format("                      Victoire !")
    print(Fore.YELLOW +combat)

def Game_Over():
    combat = pyfiglet.figlet_format("                    GAME OVER !")
    print(Fore.RED + combat )
def lvl():
    village = pyfiglet.figlet_format("                        Village")
    print(Fore.GREEN + village)
def corde():
    grotte = pyfiglet.figlet_format("                        Grotte")
    print(Fore.RED + grotte)

def duel():
    tour = pyfiglet.figlet_format("                           Tour")
    print(Fore.MAGENTA + tour)
def Go():
    debut = pyfiglet.figlet_format("Go", font='isometric1')
    print(Fore.RED+ debut )

def niv():
    niv = pyfiglet.figlet_format("Niveau         Supérieur !")
    print(Fore.YELLOW+ niv )
