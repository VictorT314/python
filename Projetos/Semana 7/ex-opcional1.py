def éPrimo(x):
    fator = 2
    if (x == 1):
        return False
    if (x == 2):
        return True
    while (x % fator != 0 and fator < x/2):
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

def n_primos(n):
    cont = 0
    i = 1
    while(i <= n):
        if (éPrimo(i) == True):
            cont = cont + 1
            i = i + 1
        else:
            i = i + 1
    return cont
        
