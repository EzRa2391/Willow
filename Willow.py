import random
menu = False
l_salles = [0,1,2,3,4,5,6,7,8,9,10,11]
adjacent = [[1,5,6],[0,2,7],[2,4,8],[3,5,9],[4,6,10],[7,11,0],[6,8,1],[7,9,2],[8,10,3],[9,11,4],[10,6,5]]

def init_game():
    # Positions initiales
    inventaire = 3
    gateau = [None, None, None]
    player = random.choice(l_salles)
    willow = random.choice(l_salles)
    c1 = random.choice(l_salles)
    c2 = random.choice(l_salles)
    p1 = random.choice(l_salles)
    p2 = random.choice(l_salles)
    
    while willow == player:
        willow =  random.choice(l_salles)
    while c1 == player or c1 == willow: 
        c1 = random.choice(l_salles)
    while c2 == player or c2 == willow or c2 == c1:
        c2 =  random.choice(l_salles)
    while p1 == player or p1 == willow or p1 == c1 or p1 == c2 :
        p1 = random.choice(l_salles)
    while p2 == player or p2 == willow or p2 == c1 or p2 == c2 or p2 == p1:
        p2 = random.choice(l_salles)

    print(player, willow, c1, c2, p1, p2, gateau, inventaire)        
    return player, willow, c1, c2, p1, p2, gateau, inventaire



# Salle de 0 à 11, commençant au W (sur l'image dans les consignes thomas)
def deplacer(player, adjacent):
    if player == 0 :
        print ("Vous pouvez vous déplacer dans les salles:", adjacent[player])
        move = int(input("Quelle salle choisissez vous ?"))
        if move == adjacent[player][0] or move == adjacent[player][1] or move == adjacent[player][2] :
            player = move
            print("Vous êtes maintenant dans la Salle",move)
            return(player)
        else :
            print ("Erreur veuillez saisir à nouveau")
            return deplacer(player)



def check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau):
    if willow == adjacent[player] and willow in gateau:
        print("Vous avez gagné")
        menu = False
        return menu
    if player == willow :
        print("PERDU, Le willow a mangé tout vous gâteaux !")
        menu = False
        return menu
    if player == c1 or player == c2:
        tp = random.choice(l_salles) 
        player = tp
        if player == willow :
            print("PERDU, Vous avez été téléporté sur le willow, il dévore tout vos gâteaux!")
            menu = False
            return menu
        
    if willow in adjacent[player]:
        print("Vous entendez un ronflement de willow qui dort en vous attendant.")
        menu = True
        return menu
    if player in adjacent[p1] or player in adjacent[p2] :
        print ("Vous ressentez un courant d'air")
        menu = True
        return menu
    if player in adjacent[c1] or player in adjacent[c2] :
        print ("Vous entendez un petit couinement")
        menu = True
        return menu



def piege(gateau, inventaire ):
    if inventaire == 0:
        print("Vous n'avez plus de gâteau")
        return
    else :
        trap = int(input("Dans quelle salle souhaitez vous posez un gateau ?"))
        if trap in gateau:
            print("Il y a déjà un gateau dans cette salle")
            return piege(gateau, inventaire)
        else:
            gateau[inventaire-1] = trap
            inventaire = inventaire-1
            return (gateau,inventaire)


def choix_menu(menu):
    if menu == True :
        return menu1(player, adjacent)
    else: 
        return menu2()

def menu1(player, adjacent):
    while True:
        print("1. Vous deplacer ")
        print("2. Poser un piège (le meilleur gateau du monde)")
        print("3. Quitter")
        rep = int(input("Que voulez vous faire?"))

        if rep in list(range(1,6)) :
            if rep==1:
                player = deplacer(player,adjacent)
        else: 
            break
    return player
    

def menu2():
    while True:
        print("1. Lancer la partie")
        print("2. Quitter")
        rep= int(input("Que voulez vous faire ? "))
        if rep==1:
            init_game()
            return(menu1())
        elif rep==2:
            print("Merci et au revoir")
            break

choix_menu(menu)