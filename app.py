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