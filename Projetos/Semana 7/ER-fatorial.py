def fatorial(x):
    if (x < 2):
        return 1
    else:
        return x * fatorial(x-1)
    
n = int(input("Insira um número: "))

while (n >= 0):
    print (fatorial(n))
    n = int(input("Insira um número: "))
