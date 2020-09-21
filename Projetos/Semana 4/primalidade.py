primo = True
i = 2

n = int(input("Digite um número inteiro: "))


if (n <= 1):
    print("não primo")
    
if (n == 2):
    print("primo")
    
if (n > 2):
    while (i < n):
        if (n % i == 0):
            primo = False
        i = i + 1
    if primo:
        print("primo")
    else:
        print("não primo")
