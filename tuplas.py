"""numeros = ("zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte")
e = int(input("Digite um número entre 0 e 20: "))
if e < 0 or e > 20:
    print("Número inválido!")
else:
    print(f"Você digitou o número {numeros[e]}")

tabela = ("flamengo", "internacional", "atlético-mg", "são paulo", "fluminense", "grêmio", "palmeiras", "santos", "atletico-go", "corinthians", "ceará", "coritiba", "bahia", "sport", "fortaleza", "vasco", "goiás", "bragantino", "botafogo", "cuiabá")
print("Os 5 primeiros colocados são:")
for c in range(0, 5):
    print(f"{c+1}º {tabela[c]}")
print("\nOs 4 últimos colocados são:")
for c in range(16, 20):
    print(f"{c+1}º {tabela[c]}")
print("\nA lista em ordem alfabética é:")
print(sorted(tabela))
print(f"\nO time do internacional está na {tabela.index('internacional')+1}ª posição")

from random import randint
maior = 0
menor = 99999999999999
ns = (randint(0, 99999999999999), randint(0, 99999999999999), randint(0, 99999999999999), randint(0, 99999999999999), randint(0, 99999999999999))
print("Os números sorteados foram: ", end="")
for n in ns:
    print(n, end=" ")
for n in ns:
    if n > maior:
        maior = n
print(f"\nO maior número sorteado foi: {maior}")
for n in ns:
    if n < menor:
        menor = n
print(f"O menor número sorteado foi: {menor}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
numero9 = 0
pares = 0

numeros = (n1, n2, n3, n4)
for i in numeros:
    if i == 9:
        numero9 += 1
    if i % 2 == 0:
        pares += 1


print (f'o numero 9 apareceu {numero9} vezes')
for pos, valor in enumerate(numeros):
    if valor == 3:
        print(f'o número 3 apareceu na {pos+1}ª posição')
        achou3=True
    if not achou3:
        print('o número 3 não foi digitado')
print(f"foram digitados {pares} números pares")"""

produtosPreco = ("Lápis", 1.50, "Borracha", 0.75, "Caderno", 12.00, "Mochila", 150.00)
print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
for pos in range(0, len(produtosPreco), 2):
    print(f"{produtosPreco[pos]:.<30}R${produtosPreco[pos+1]:>6.2f}")