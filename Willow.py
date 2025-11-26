Player = "Salle0"

def Joueur(Player):
    if Player == "Salle0":
        print ("Vous pouvez vous déplacer dans les salles 6, 9, et 12")
        Move = int(input("Quelle salle choisissez vous ?"))
        if Move == 1 or Move == 9 or Move == 12:
            Player = str("Salle"+Move)
            print("Vous êtes maintenant dans la",Player)
            return(Player)
        else :
            print ("Erreur veuillez saisir à nouveau")
            return Joueur(Player)
    if Player == "Salle1":
        return
    if Player == "Salle2":
        return
    if Player == "Salle3":
        return
    if Player == "Salle4":
        return
    if Player == "Salle5":
        return
    if Player == "Salle6":
        return
    if Player == "Salle7":
        return
    if Player == "Salle8":
        return
    if Player == "Salle9":
        return
    if Player == "Salle10":
        return
    if Player == "Salle11":
        return
    if Player == "Salle12":
        return
    
Joueur("Salle0")


# check si Player est sur méchant ou si méchant et proche etc ...

# def méchant
