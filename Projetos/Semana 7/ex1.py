largura = 1
altura = 1

l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

while (altura <= a):
    while (largura <= l):
        print("#", end = "")
        largura = largura + 1
    altura = altura + 1
    print ()
    largura = 1
