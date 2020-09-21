lista = []
i = 0

n = int(input("Digite um número: "))

while (n != 0):
    lista.append(n)
    i = i + 1
    n = int(input("Digite um número: "))

if (n == 0):
    print()
    while (i > 0):
        print (lista[i-1])
        i = i - 1
