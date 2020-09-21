import math

def delta(a, b, c):
    return float(b**2 - (4*a*c))

def eq_2_grau():
    a = float(input("Digite o valor de 'a' da equação: "))
    b = float(input("Digite o valor de 'b' da equação: "))
    c = float(input("Digite o valor de 'c' da equação: "))
    raizes(a, b, c)

def raizes(a, b, c):
    d = delta(a, b, c)
    if d > 0 and a != 0:
        x1 = (-b - math.sqrt(d))/2*a
        x2 = (-b + math.sqrt(d))/2*a
        print("as raízes da equação são",x1,"e",x2)

    if d == 0 and a != 0:
        x1 = -b/2*a
        print("a raiz desta equação é",x1)

    if d < 0:
        print("esta equação não possui raízes reais")
