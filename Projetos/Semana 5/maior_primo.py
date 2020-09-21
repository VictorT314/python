def maior_primo(n):
    x=0
    y=n #começar do cima para baixo para poder sair no primeiro primo

    while y>=1: #ciclo agora ao contrario até 1
        for x in range(2, y + 1): #range nao inclui o ultimo, logo tem de ser y +1
            if y % x == 0:
                break

        if x == y: #se chegou até y é porque nao deu para dividir por nenhum, logo primo
            return x

        y = y - 1

    return 1 #se nao deu para achar nenhum primo retorna-se um
