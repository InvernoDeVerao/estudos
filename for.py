"""from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
print("EXPLUDIU O FOGO DE ARTIFICIL!! UAU")

pares = []
for i in range(0, 51):
    if i % 2 == 0:
        pares.append(i)
print(f"esses são os numeros pares de 0 a 50 :{pares}")

s = 0
for i in range(0, 501):
    if i % 2 != 0 and i % 3 == 0:
        s += i
print(f"A soma dos números ímpares e múltiplos de 3 entre 0 e 500 é: {s}")

n1 = int(input("Digite um número inteiro: "))
divisores = 0
for i in range(1, n1 +1):
    if n1 % i == 0:
        divisores += 1

if divisores == 2:
    print(f"O número {n1} é primo.")
else:
    print(f"O número {n1} não é primo.")

palavra = input("Digite uma palavra: ").lower().replace(" ", "")
inverso = ''
for i in range(len(palavra) - 1, -1, -1):#len(palavra) - 1 = última posição da palavra, -1 é o passo para trás, ou seja, vai percorrer a palavra de trás para frente.

    inverso += palavra[i]


if palavra == inverso:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")"""
