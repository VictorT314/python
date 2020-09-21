# Variáveis
usuario = True
computador = True
n = 0
m = 0
e = 0
c = 0
j= 0
opcao = 0

#Funções

def computador_escolhe_jogada():
    global n
    global e
    
    c = (n % e)
    n = n - c
    
    if (n >= 2):
        if (c > 1):
            print("\nO computador tirou",c,"peças.")
            print("Agora restam",n,"peças no tabuleiro.\n")
        if (c == 1):
            print("\nO computador tirou uma peça.")
            print("Agora restam",n,"peças no tabuleiro.\n")
    else:
        if (c > 1):
            print("O computador tirou",c,"peças.")
            print("Fim de Jogo! O computador ganhou!\n")
        if (c == 1):
            print("O computador tirou uma peça.")
            print("Fim de jogo! O computador ganhou!\n")

def usuario_escolhe_jogada():
    global n
    
    j = int(input("Quantas peças você vai tirar? "))
    
    while (j > n or j <= 0 or j > m):
        print("\nOops! Jogada inválida! Tente de novo.")
        j = int(input("\nQuantas peças você vai tirar? "))

    n = n - j
    
    if (n >= 2):
        if (j > 1):
            print("\nVocê tirou",j,"peças.")
            print("Agora restam",n,"peças no tabuleiro.\n")
        if (j == 1):
            print("\nVocê tirou uma peça.")
            print("Agora restam",n,"peças no tabuleiro.\n")
    else:
        if (j > 1):
            print("\nVocê tirou",j,"peças.")
            print("Agora resta apenas uma peça no tabuleiro.\n")
        if (j == 1):
            print("\nVocê tirou uma peça.")
            print("Agora resta apenas uma peça no tabulerio.\n")

def partida():
    global opcao
    global m
    global n
    global e
    global c
    global j
    global usuario
    global computador
    
    
    n = int(input("Quantas peças? "))
    while(n <= 0):
        print("Número de peças inválido!\n")
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while (m >= n):
        print("O numero de peças por jogada deve ser menor do que o número de peças!\n")
        m = int(input("Limite de peças por jogada? "))
    e = m + 1
    if (n % e == 0):
        print("\nVocê começa!\n")
        while(n > 0 and usuario):
            usuario_escolhe_jogada()
            computador_escolhe_jogada()
            if (n == 0):
                usuario = False
    else:
        print("\nComputador começa!")
        while (n > 0 and computador):
            computador_escolhe_jogada()
            if (n == 0):
                computador = False
                break
            usuario_escolhe_jogada()
            
    usuario = True
    computador = True
        
def campeonato():
    print("\nVocê escolheu campeonato!")
    print("\n**** Rodada 1 ****\n")
    partida()
    print("**** Rodada 2 ****\n")
    partida()
    print("**** Rodada 3 ****\n")
    partida()
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador")
        
    
# Jogo

print("\nBem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
opcao = int(input("2 - para jogar um campeonato "))
while(opcao != 1 and opcao != 2):
    opcao = int(input("\nOops! Opção inválida! Tente de novo: "))

if (opcao == 1):
    print("\nVocê escolheu uma partida!\n")
    partida()

else:
    campeonato()

        
        
