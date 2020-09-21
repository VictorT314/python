soma = 0

n = int(input("Digite um número inteiro: "))

if (n < 0):
    n = -n

while (n % 10 <= 9 and n > 0):
    soma = soma + n % 10
    n = n // 10
    
print (soma)
