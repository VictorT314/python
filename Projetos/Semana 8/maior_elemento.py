def maior_elemento(lista):
    try:
        if len(lista) == 0:
            return None

        maior = lista[0]

        for valor in lista:
            if valor > maior:
                maior = valor

        return maior
    except TypeError:
        return lista
