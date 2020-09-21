import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n")

    tamMedPalavra = float(input("Entre o tamanho medio de palavra: "))
    typeToken = float(input("Entre a relação Type-Token: "))
    hapaxLegomana = float(input("Entre a Razão Hapax Legomana: "))
    tamMedSentenca = float(input("Entre o tamanho médio de sentença: "))
    comMedSentenca = float(input("Entre a complexidade média da sentença: "))
    tamMedFrase = float(input("Entre o tamanho medio de frase: "))

    print()

    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):    
    somatorio = 0
    for i in range(len(as_a)):
        somatorio += abs(as_a[i] - as_b[i])

    return somatorio / 6
        

def calcula_assinatura(texto):    
    sentencas = separa_sentencas(texto)
    num_sentencas = 0
    soma_car_sentencas = 0

    frases = []
    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.append(frase_aux)
        num_sentencas += 1
        soma_car_sentencas = soma_car_sentencas + len(sentencas[i])

    palavras = []
    num_frases = 0
    soma_car_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)
            num_frases += 1
            soma_car_frases += len(frases[linha][coluna])

    mtrx_para_lista = []
    #COLOCA O QUE ESTÁ NA EM MATRIZ PARA UMA LISTA
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            mtrx_para_lista.append(palavras[linha][coluna])
    palavras = mtrx_para_lista[:]

    total_letras = 0
    num_tot_palavras = len(palavras)
    #CALCULA A QUANTIDADE DE LETRAS
    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras = total_letras + len(str(palavras[lin][col]))
    
    tamMedPalavra = total_letras / num_tot_palavras
    typeToken = n_palavras_diferentes(palavras) / num_tot_palavras
    hapaxLegomana = n_palavras_unicas(palavras) / num_tot_palavras
    tamMedSentenca = soma_car_sentencas / num_sentencas
    comMedSentenca = num_frases / num_sentencas
    tamMedFrase = soma_car_frases / num_frases
    
    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]



def avalia_textos(textos, assinaturaMain):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []
    for i in textos:
        assinaturas.append(calcula_assinatura(i))

    similaridade = []
    for i in assinaturas:
        similaridade.append(compara_assinatura(assinaturaMain, i))

    maior = similaridade[0]
    posicao = 0
    for i in range(len(similaridade)):        
        if similaridade[i] > maior:
            maior = similaridade[i]
            posicao = i

    return posicao

'''Minhas funções'''
def main():
    assinaturaMain = le_assinatura()
    textos = le_textos()
    
    return  print("O autor do texto " , avalia_textos(textos, assinaturaMain), " está infectado com COH-PIAH")
