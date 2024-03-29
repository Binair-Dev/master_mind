

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


