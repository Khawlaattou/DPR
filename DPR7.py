def DPR(T, x):
    n = 0
    if len(T) == 0:
        return 0
    elif len(T) == 1:
        if T[0] == x:
            return 1
        else:
            return 0
    else:
        mid = len(T) // 2
        gauche = DPR(T[:mid], x)
        droite = DPR(T[mid:], x)
        n = gauche + droite
    return n



