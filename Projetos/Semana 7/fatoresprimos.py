n = int(input("Digite um número inteiro maior do que 1: "))

fator = 2
multiplicidade = 0

while (n > 1):
    while (n % fator == 0):
        multiplicidade = multiplicidade + 1
        n = n / fator
    if (multiplicidade > 0):
        print("fator ", fator, "multiplicidade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0
