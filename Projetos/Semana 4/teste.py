soma = 0
i = 1
valor = 0

n = int(input("Digite o número de elementos da sequência: "))

while (i <= n):
    valor = int(input("Digite um elemento da sequência: "))
    soma = soma + valor
    i = i + 1

print("A soma dos elementos da sequência é:", soma)
