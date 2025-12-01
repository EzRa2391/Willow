# Importation des packages
import random
import os
import time

# Définition des constantes menu, l_salles et adjacent
menu = False
l_salles = [0,1,2,3,4,5,6,7,8,9,10,11]
adjacent = [[1,5,6],[0,2,7],[1,3,8],[2,4,9],[3,5,10],[4,6,11],[7,11,0],[6,8,1],[7,9,2],[8,10,3],[9,11,4],[10,6,5]]

#Fonction de l"initialisation de la partie
def init_game(adjacent):
    # Attribution aléatoires des positions initiales
    os.system("cls" if os.name == "nt" else "clear") # Nettoyage console
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
        print ("Erreur veuillez saisir à nouveau !") # Gestion de l"erreur
        return deplacer(player, adjacent)


# Fonction pour vérifier les positions des élèments entre-eux a la fin d"un tour.
def check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire):
    menu = True
    if willow in adjacent[player] and willow in gateau: # Conditions de victoire
        print("\nGAGNÉ, Vous avez capturé le Willow ! \n")
        menu = False
        return menu, player
    elif player == willow : # Condition de défaite
        print("\nPERDU, Le willow a mangé tout vous gâteaux ! \n")
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
            print("\nPERDU, La téléportation a réveillé le willow, et il a dévoré tout vos gâteaux! \n")
            menu = False
            return menu, player
        elif player == p1 or player == p2 : # Si le joueur a été téléporté sur un puit
            print("\nPERDU, Vous avez été téléporté au dessus d'un puit, vous tombez dedans, plouf! \n")
            menu = False
            return menu, player
        else : # Si tout va bien
            check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
            return menu, player
    elif player == p1 or player == p2: #Si le joueur finit son tour sur un puit
        print("\nPERDU, Vous êtes tombé dans le puit ! \n")
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
    menu = True
    if inventaire == 0:
        print("Vous n'avez plus de gâteau")
        return gateau,inventaire,willow,player,menu
    else : # Différents cas de figure suite au jet du gâteau
        trap = int(input("Dans quelle salle souhaitez vous posez un gâteau ? "))
        if trap in gateau:
            print("Il y a déjà un gâteau dans cette salle")
            return piege(gateau, inventaire, willow, adjacent, player)
        elif trap in l_salles :
            gateau.append(trap)
            inventaire = inventaire-1
            print("Attention, Le Willow se réveille !")
            time.sleep(1)
            if willow in adjacent[player] and willow in gateau:
                print("\nLe Willow se penche pour manger la part de gâteau ! \n")
                menu = False
                return gateau,inventaire,willow,player,menu
            else :
                print("Vous avez loupé le Willow, vous attendez sa réaction :")
                coinflip = random.randint(0, 1)
                if coinflip == 0 :
                    print("Le Willow décide de chercher le gâteau et il bouge dans une salle adjacente !")
                    willow = random.choice(adjacent[willow])
                    if willow == player :
                        print("\nPERDU, malheuresement le willow s'est déplacé dans votre salle, et vous a mangé !\n")
                        menu = False
                        return gateau,inventaire,willow,player,menu
                    else :
                        print("Vous êtes sauvé, le Willow n'est pas rentré dans votre salle !")
                else :
                    print("Le Willow ne fait rien et se rendort !")
    print(" ")
    time.sleep(1)
    return gateau, inventaire, willow, player, menu


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

def regle():
    peuplier = True
    malicieux = True
    while peuplier == True :
        print(" ")
        choix = str(input("Choisissez les règles que vous voulez voir : Victoire | Messages | Traquenards | Déplacement | Gateau | Quitter | : ")) #traquenard
        dico_traquenards = {"Souris": "Si vous entrez dans une pièce occupée par une de ces charmantes bestioles,"
                            "elle vous le fera payer très cher,\n en vous jetant un sort qui vous transporta aléatoirement"
                            "dans n’importe quelle autre pièce...\n et peut-être celle où se tapit Willow. Si vous entrez dans la pièce où se cache Willow," 
                            "\npar étourderie ou par vengeance d’une des souris il dévorera tous vos gateaux et aura gagné...!!!\n", 
                            "Puits" : "Vous pouvez, toujours par étourderie, tomber dans un des deux puits"
                            " à moins que ce soit la souris qui vous y jette\n"}
        dico = {"Victoire": "Ce jeu consiste à vaincre Willow, un étrange habitant d’un labyrinthe, en le capturant grâce à un gateau auquel il ne pourra résister."
                "La tanière dans laquelle s’est réfugié Willow est constituée des 12 pièces réunies par des couloirs. Willow dort dans l’une de ces pièces. "
                "Vous vous déplacez de pièce en pièce en passant par les couloirs. Pour capturer Willow, "
                "il faut être dans une pièce contiguë à la sienne et sortir un gâteau pour l’attirer, vous en avez 3 à votre disposition.", 
                "Messages" : "Lors de votre partie vous pourrez recevoir certains messages, voici les conditions selon le message :\n"
                "• Si vous êtes seulement distant d’une case de Willow (cas de X1), vous recevez un message : un ronflement de Willow qui dort en vous attendant.\n"
                "• Si vous êtes seulement distant d’une case d’un puit le message sera : un courant d’air.\n"
                "• Si vous êtes seulement distant d’une case d’une souris le message sera : un petit couinement.\n",
                "Déplacements": "La tanière de Willow est constituée des 12 pièces réunies par des couloirs, vous pouvez vous déplacer seulement dans les pièces adjacentes.",
                "Gateau" : " Le jouer peut jeter un gâteau dans n'importe quelle salle depuis n'importe quelle salle,"
                " Mais attention ! Chaque fois que vous jeterez un gateau cela réveillera le Willow, à ce moment là son comportement est incertain,"
                "il pourra tout autant se déplacer que se rendormir, donc gare à vous si vous êtes dans les parages !"
                "De plus vous ne pourrez emportez que 3 parts de gâteaux avec vous dans la tanière"
        }
        if choix == "Quitter":
            peuplier = False
            return
        elif choix == "Traquenards":
            print(" ")
            while malicieux == True :
                print("Sous-menu traquenards : Souris | Puits | Quitter ")
                rep = str(input("Choisissez le traquenard pour avoir plus d'info : "))
                if rep in dico_traquenards.keys():
                    print("\n",dico_traquenards[rep])
                elif rep == "Quitter" :
                    malicieux = False
                else : print("Vous avez fait une erreur de saisie, veillez réessayer !")        
        elif choix in dico.keys():
            print("\n",dico[choix])
        else :
            "Vous avez fait une erreur de saisie, veuillez réessayer !"




# Fonction du menu dans le jeu
def menu1():
    n=1
    pouet = True
    player, willow, c1, c2, p1, p2, gateau, inventaire = init_game(adjacent)
    pouet, player = check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
    while pouet == True:
        time.sleep(1)
        afficherstat(player, adjacent, gateau, inventaire)
        time.sleep(3)
        print("=========================== Tour",n,"===============================")
        print("1. Se déplacer | 2. Poser un piège | 3. Afficher la carte | 4. Retour au menu principal")
        n = n+1
        rep = int(input("Que voulez vous faire? "))
        if rep == 1:
            time.sleep(1)
            player = deplacer(player, adjacent)
        elif rep == 2:
            gateau, inventaire, willow, player, pouet = piege(gateau, inventaire, willow, adjacent, player)
        elif rep == 3:
            time.sleep(1)
            carte()
        elif rep == 4:
            print(" ")
            break
        else:
            print("Choix invalide !")
        time.sleep(1)
        pouet, player = check_positions(player, adjacent, c1, c2, p1, p2, willow, gateau, inventaire)
    pouet = False
    return

# Fonction du Menu principal pour lancer ou quitter le jeu
def menu2():
    os.system("cls" if os.name == "nt" else "clear") # Nettoyage console
    print("////////////////////////////////////")
    print("      LE LABYRINTHE DE WILLOW")
    print(" by Hugard Thomas & Trévinal Victor")
    print("//////////////////////////////////// \n")
    while True:
        time.sleep(1)
        print("1. Lancer la partie | 2. Règles du jeu | 3. Quitter")
        rep= int(input("Que voulez vous faire ? "))
        if rep==1:
            menu1()
        elif rep==2:
            regle()
        elif rep==3:
            print("Merci et au revoir !")
            break
        else :
            print("Erreur de saisie !")
# Appel de la fonction menu2() : lancement du menu principal.
menu2()