import ascii
import game
from colorama import Fore

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
    ascii.new_game()
    print(Fore.YELLOW + "🐷Maitre Cochon a dit un jour: 'Seuls les Héros🧝‍ qui se battent pour une noble cause sont amenés à rentrer dans l'Histoire.' ")
    input("\nAppuyez sur ENTREE pour continuer...")
    ascii.barre()
    print(Fore.CYAN +"Bienvenue sur Earth Quest ! Si tu es ici, c'est que tu as forcément entendu parler du danger qui menace notre monde ! ")
    print(Fore.CYAN +"Autrfois sur la planète Dyflo, les royaumes de Sunir et de Xebe vivaient en paix. Quelques années passèrent, ils finirent par épuiser les ressources de notre planète... ")
    print(Fore.CYAN +"La paix laissa place à une guerre de ressources. Malgré la victoire de Sunir, quelques Xebe survivèrent et gardèrent rancune contre Sunir...")
    print(Fore.CYAN+"Aujourd'hui, des siècles plus tard, notre planète arrive au point de ne plus pouvoir héberger de vies humaines.")
    input("\nAppuyez sur ENTREE pour continuer...")
    ascii.barre()
    print('')
    print(Fore.CYAN +"Le seul espoir est une pierre légendaire appelée 💎 pierre d'Hope capable de transporter tout un peuple sur une autre planète.")
    print(Fore.CYAN +"Tu dois battre le 💀 boss final qui est le dernier descedant de Xebe : Hypérion et sa rancune envers Sunir et trouver la pierre pour tous nous sauver !" "\n")
    print(Fore.YELLOW + "🐷Maitre Cochon : 'Ne t'inquiètes pas ! Je vais t'accompagner durant cette quete ! Tu ne seras pas seul !'")
    print(Fore.CYAN + "Bonne chance Héros ! ")
    print('')
    input("\nAppuyez sur ENTREE pour continuer...")
    name = str(input(Fore.BLUE + "\nPour écrire l'Histoire, il faut qu'on se souvienne de toi ! : Quel est ton nom ?  "  ))#demander de choisir une nom
    save() #sauvegarde automatique grace a la fonction save
    ascii.clear()
    ascii.barre()
    print(Fore.BLUE + '       Bienvenue Héros ', name, '!')
    ascii.barre()
    print('')
    print("       La partie est sauvegardee\n")
    print('')
    ascii.barre()
    input("\nAppuyez sur ENTREE pour continuer...")
    game.game()
