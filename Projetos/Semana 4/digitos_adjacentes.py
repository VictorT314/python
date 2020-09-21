
i = 0
adjacente = False

x = int(input("Digite um número inteiro: "))
n = x

if ((n % 10) == 0 and n != 0):
    while (n > 0):
        n = x % 10
        i = (x // 10) % 10
        x = x // 10
    if (n == i):
        adjacente = True
else:
    while (x // 10 != 0):
        n = x % 10
        i = (x // 10) % 10
        if (n == i):
            adjacente = True
        x = x // 10
    
if adjacente:
    print("sim")
else:
    print("não")
