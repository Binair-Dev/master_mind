
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