def moy(tps):
    m = 0
    if len(tps) == 0:
        return 0
    elif len(tps) == 1:
        m = tps[0]
    else:
        sm = sum(tps)  
        m = sm / len(tps)
    return m