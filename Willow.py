# Importation des packages
import random
import os

# Définition des constantes menu, l_salles et adjacent
menu = False
l_salles = [0,1,2,3,4,5,6,7,8,9,10,11]
adjacent = [[1,5,6],[0,2,7],[1,3,8],[2,4,9],[3,5,10],[4,6,11],[7,11,0],[6,8,1],[7,9,2],[8,10,3],[9,11,4],[10,6,5]]

#Fonction de l'initialisation de la partie
def init_game(adjacent):
    # Attribution aléatoires des positions initiales
    os.system('cls' if os.name == 'nt' else 'clear') # Nettoyage console
    inventaire = 3
    gateau = []
    player = random.choice(l_salles)
    willow = random.choice(l_salles)
    c1 = random.choice(l_salles)
    c2 = random.choice(l_salles)
    p1 = random.choice(l_salles)
    p2 = random.choice(l_salles)
    
    # Vérification des chevauchements des positions et des éventuels blocages
    while willow == player:
        willow =  random.choice(l_salles)
    while c1 == player or c1 == willow: 
        c1 = random.choice(l_salles)
    while c2 == player or c2 == willow or c2 == c1:
        c2 =  random.choice(l_salles)
    while p1 == player or p1 == willow or p1 == c1 or p1 == c2 :
        p1 = random.choice(l_salles)
    while p2 == player or p2 == willow or p2 == c1 or p2 == c2 or p2 == p1 or p2 in adjacent[player]:
        p2 = random.choice(l_salles)

    #print(player, willow, c1, c2, p1, p2, gateau, inventaire) #Pour débuguer      
    return player, willow, c1, c2, p1, p2, gateau, inventaire



# Fonction de déplacement du joueur selon son choix.
def deplacer(player, adjacent):
    print ("Vous pouvez vous déplacer dans les salles:", adjacent[player])
    move = int(input("Quelle salle choisissez-vous ? "))
    print("==================================================================", "\n")
    if move in adjacent[player] :
        player = move
        return(player)
    else :
        print ("Erreur veuillez saisir à nouveau !") # Gestion de l'erreur
        return deplacer(player, adjacent)


# Fonction pour vérifier les positions des élèments entre-eux a la fin d'un tour.
def check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire):
    menu = True
    if willow in adjacent[player] and willow in gateau: # Conditions de victoire
        print("GAGNÉ, Vous avez capturé le Willow !")
        menu = False
        return menu, player
    elif player == willow : # Condition de défaite
        print("PERDU, Le willow a mangé tout vous gâteaux !")
        menu = False
        return menu, player
    elif player == c1 or player == c2: #Si le joueur rencontre une souris magique
        tp = random.choice(l_salles)
        while tp == c1 or tp == c2:
            tp = random.choice(l_salles)
        player = tp
        print("Vous êtes rentré dans la salle d'une souris magique, elle vous téléporte en salle",player)
        print(" ")
        if player == willow : # Si le joueur a été téléporté sur le Willow
            print("PERDU, La téléportation a réveillé le willow, et il a dévoré tout vos gâteaux!")
            menu = False
            return menu, player
        elif player == p1 or player == p2 : # Si le joueur a été téléporté sur un puit
            print("PERDU, Vous avez été téléporté au dessus d'un puit, vous tombez dedans, plouf!")
            menu = False
            return menu, player
        else : # Si tout va bien
            check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
            return menu, player
    elif player == p1 or player == p2: #Si le joueur finis son tour sur un puit
        print("PERDU, Vous êtes tombé dans le puit !")
        menu = False
        return menu, player
    
    # Vérification des placements adjacents au joueur
    elif willow in adjacent[player]:
        print("Vous entendez un ronflement de willow qui dort en vous attendant.")
    elif player in adjacent[p1] or player in adjacent[p2] :
        print ("Vous ressentez un courant d'air")
    elif player in adjacent[c1] or player in adjacent[c2] :
        print ("Vous entendez un petit couinement")
    elif willow in gateau and willow not in adjacent[player] :
        print ("Le Willow a dévoré un gâteau qui traînait par terre")
        del gateau[willow]
    else:
        print("Vous ne ressentez rien d'anormal aux alentours")
    return menu, player



# Fonction pour poser les gâteaux
def piege(gateau, inventaire, willow, adjacent, player):
    if inventaire == 0:
        print("Vous n'avez plus de gâteau")
        return
    else : # Différents cas de figure suite au jet du gâteau
        trap = int(input("Dans quelle salle souhaitez vous posez un gateau ? "))
        if trap in gateau:
            print("Il y a déjà un gâteau dans cette salle")
            return piege(gateau, inventaire)
        else:
            gateau.append(trap)
            inventaire = inventaire-1
            print("Attention, Le Willow se réveille !")
            willow = random.choice(adjacent[willow])
            if willow in adjacent[player] and willow in gateau:
                print("GAGNÉ, Vous avez capturé le Willow !")
                menu = False
                return menu, player
            else :
                print("Vous avez loupé le Willow, vous attendez sa réaction :")
                coinflip = random.randint(0, 1)
                if coinflip == 0 :
                    print("Le Willow décide de chercher le gâteau et il bouge dans une salle adjacente !")
                    willow = random.choice(adjacent[willow])
                    if willow == player :
                        print("PERDU, malheuresement le willow s'est déplacé dans votre salle, et vous a mangé !")
                        menu = False
                        return menu, player
                    else :
                        print("Vous êtes sauvé, le Willow n'est pas rentré dans votre salle !")

                else :
                    print("Le Willow ne fait rien et se rendort !")
            return (gateau,inventaire)



# fonction pour récapituler la situation du joueur dans le labyrinthe
def afficherstat(player, adjacent, gateau, inventaire):
    if gateau == [] :
        print("Vous êtes maintenant dans la salle",player,"\n",
            "Vous êtes proche des salles",adjacent[player],"\n",
            "Il vous reste",inventaire,"gâteaux,","et vous n'avez pas posé de gâteau !")
        print(" ")
        return
    elif len(gateau) == 1 :
        print("Vous êtes maintenant dans la salle",player,"\n",
            "Vous êtes proche des salles",adjacent[player],"\n",
            "Il vous reste",inventaire,"gâteaux,","et vous avez posé des gâteaux dans la salle",gateau)
        print(" ")
        return
    else:
        print("Vous êtes maintenant dans la salle",player,"\n",
            "Vous êtes proche des salles",adjacent[player],"\n",
            "Il vous reste",inventaire,"gâteau,","et vous avez posé des gâteaux dans les salles",gateau)
        print(" ")
        return


# Fonction pour afficher la carte du labyrinthe de Willow
def carte():
    print("==================================================================", "\n")
    print("Le labyrinthe de Willow")
    print(r" 6-----7-----8")
    print(r" |\    |    /|")
    print(r" | 0---1---2 |")
    print(r" | |       | |")
    print(r" | 5---4---3 |")
    print(r" |/    |    \|")
    print(r" 11----10----9")
    print(" ")

# Fonction du menu dans le jeu
def menu1():
    n=1
    pouet = True
    player, willow, c1, c2, p1, p2, gateau, inventaire = init_game(adjacent)
    pouet, player = check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
    while pouet == True:
        afficherstat(player, adjacent, gateau, inventaire)
        print("=========================== Tour",n,"===============================")
        print("1. Se déplacer | 2. Poser un piège | 3. Afficher la carte | 4. Retour au menu principal")
        n = n+1
        rep = int(input("Que voulez vous faire? "))
        if rep == 1:
            player = deplacer(player, adjacent)
        elif rep == 2:
            gateau, inventaire = piege(gateau, inventaire, willow, adjacent, player)
        elif rep == 3:
            carte()
        elif rep == 4:
            print(" ")
            break
        else:
            print("Choix invalide.")
        pouet, player = check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
    pouet = False
    return

# Fonction du Menu principal pour lancer ou quitter le jeu
def menu2():
    while True:
        print("1. Lancer la partie | 2. Quitter")
        rep= int(input("Que voulez vous faire ? "))
        if rep==1:
            menu1()
        elif rep==2:
            print("Merci et au revoir")
            break

# Appel de la fonction menu2() : lancement du menu principal.
menu2()