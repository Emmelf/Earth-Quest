import ascii


#cette fonction est en bonus au cas ou le jeu n'est pas assez clair comme il n'y a pas de map visuelle


def indice():
    
    f = open('load.txt', 'r')
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
    
    if bomb == 0:
        print('Trouvez un village en x : 1, y : 2')
    if bomb == 1:
        print('Trouvez une grotte en x : 5, y : 1')
    if bomb == 2:
        print('Trouvez la tour en x : 4, y : 3')