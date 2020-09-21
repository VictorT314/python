def fatorial(x):
    if (x < 2):
        return 1
    else:
        return x * fatorial(x-1)
def binomio(n,k):
    return (fatorial(n)) / (fatorial(k) * fatorial(n-k))
