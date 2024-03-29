def evaluer(couleur):
    check = []
    for _ in range(5):
        check.append(colorPick())

    check1 = set()
    check2 = []
    for i, res in enumerate(check):
        for j,resp in enumerate(couleur):
            if res[i] == resp[j]:
                check1.add(res[i])
            elif res in check:
                check2.append(res)

    if len(check1) == 3:
        return True
    elif check2:
        return check2
    else:
        return False

def game_loop():
    move_left = 10
    color_picked = 0
    master_mind_color = list()
    running = True

    print("[M] Choix du code")
    while color_picked < 4:
        master_mind_color.append(colorPick())  
        color_picked += 1
    
    while move_left > 0 and running:
        print("[J] Deviner le code")
        running = not evaluer(master_mind_color)
        move_left -= 1

if __name__ == "__main__":
    game_loop()

def colorPick():
    userInput = input("Veuillez sélectionner une couleur:")
    userInput.strip().lower()
    return userInput;

def colorPicks():
    colors = ["blanc", "bleu", "rouge", "vert", "jaune", "orange", "mauve", "brun"]
    picked = []
    while len(picked) < 4:
        userInput = input("Veuillez entrer une couleur:").strip().lower()
        if userInput in colors:
            print("Couleur ajoutée.")
            picked.append(userInput)
        else:
            print(f"Couleur invalide ! Voici les couleurs: {colors}")
    return picked

