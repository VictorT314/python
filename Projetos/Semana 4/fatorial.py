fatorial = 1
i = 1

n = int(input("Digite o valor de n: "))

if (n == 0):
    print("1")
else:
    while (i <= n):
        fatorial = fatorial * i
        i = i + 1
    print(fatorial)

