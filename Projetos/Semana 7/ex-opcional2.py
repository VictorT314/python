def é_hipotenusa(n):
    hipotenusa = False
    i = 1
    j = 1
    while (i <= n):
        while(j <= n):
            if (n ** 2 == i ** 2 + j ** 2):
                return not hipotenusa
            j = j + 1
        i = i + 1
        j = 1
    if (i >= n and (not hipotenusa)):
        return False
        
def soma_hipotenusas(n):
    soma = 0
    a = 1
    while (a <= n):
        if (é_hipotenusa(a) == True):
            soma = soma + a
            a = a + 1
        else:
            a = a + 1
    return soma
