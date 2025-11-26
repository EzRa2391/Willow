import random
L_Salles = [0,1,2,3,4,5,6,7,8,9,10,11]

def init_game():
    
    # Positions initiales
    Player = random.choice(L_Salles)
    Willow =  random.choice(L_Salles)
    while Willow == Player:
        Willow =  random.choice(L_Salles)
    while C1 == Player or C1 == Willow: 
        C1 = random.choice(L_Salles)
    while C2 == Player or C2 == Willow or C2 == C1:
        C2 =  random.choice(L_Salles)
    return Willow, C1, C2

# Salle de 0 à 11, commençant au W (sur l'image dans les consignes thomas)
def Joueur(Player):
    if Player == 0 :
        print ("Vous pouvez vous déplacer dans les salles 1, 5, et 6")
        Move = int(input("Quelle salle choisissez vous ?"))
        if Move == 1 or Move == 5 or Move == 6:
            Player = Move
            print("Vous êtes maintenant dans la Salle",Move)
            return(Player)
        else :
            print ("Erreur veuillez saisir à nouveau")
            return Joueur(Player)
    if Player == 1 :
        return
    elif Player == 2 :
        return
    elif Player == 3 :
        return
    elif Player == 4 :
        return
    elif Player == 5 :
        return
    elif Player == 6 :
        return
    elif Player == 7 :
        return
    elif Player == 8 :
        return
    elif Player == 9 :
        return
    elif Player == 10 :
        return
    elif Player == 11 :
        return

def check_positions():
    if Player == Willow
        print("Vous avez  !")
        return
    if Player == C1 or Player == C2:
        TP = random.choice(L_Salles) 
        Player = TP
        if Player == Willow
            print("Vous avez été téléporté sur le Willow, il dévore tout vos gateaux!")
            return



# check si Player est sur méchant ou si méchant et proche etc ...

# def méchant

# def Menu1():
#     print("1. Vous deplacer ?")
#     print("2. Poser le spike ?")
#     print("3. Afficher les réactions d'une enzyme")
#     print("4. Afficher les réactions d'un métabolite")
#     print("5. Quitter")

# while True:
#     Menu1()
#     rep= int(input("que voulez vous faire ?"))
#     if rep==1:
#         creerReaction()
#     elif rep==2:
        
#     elif rep==3:
#         query=input("Quelle enzyme recherchez-vous ?")
#         afficherReaction(query)
#     elif rep==4:
#         querymeta=input("Quel métabolite recherchez-vous ?")
#         affichemetabolite(querymeta)
#     elif rep==5:
#         break

# def Menu2():
#     print("1. Vous deplacer ?")
#     print("2. Afficher les réactions d'une enzyme")
#     print("3. Afficher les réactions d'un métabolite")
#     print("4. Quitter")

# while True:
#     Menu2()
#     rep= int(input("que voulez vous faire ?"))
#     if rep==1:
#         creerReaction()
#     elif rep==2:
        
#     elif rep==3:
#         query=input("Quelle enzyme recherchez-vous ?")
#         afficherReaction(query)
#     elif rep==4:
#         querymeta=input("Quel métabolite recherchez-vous ?")
#         affichemetabolite(querymeta)
#     elif rep==5:
#         break