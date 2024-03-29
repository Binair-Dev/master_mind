def evaluer(couleur):
    check = []
    for _ in range(5):
        check.append(colorPick())

    check2 = []
    for res in couleur:
        for choice in check:
            if res == choice:
                check2.append(choice)

    resultat = len(check2)
    if resultat == 4:
        return True
    else:
        return False










    return check

3 = COULEUR MASTERMIND
ENTREE TABLEAU
SORTIE = VRAI