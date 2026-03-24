"""a = [1, 2, 3]
b = a #ele faz ligação da lista a com a lista b, ou seja, se eu mudar a, b também muda
b.append(4) #adiciona o número 4 na lista b, mas como a e b estão ligadas, o número 4 também é adicionado na lista a
print(f"Lista a: {a}")
print(f"Lista b: {b}")

c = a[:] #ele faz uma cópia da lista a para a lista c, ou seja, se eu mudar a, c não muda
c.append(5) #adiciona o número 5 na lista c, mas como a e c não estão ligadas, o número 5 não é adicionado na lista a
print(f"Lista a: {a}")
print(f"Lista c: {c}")

n = []

for _ in range(5):
    n.append(int(input("Digite um número: ")))

maior = menor = n[0]

for i in n:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

pos_maior = []
pos_menor = []

for i, v in enumerate(n):
    if v == maior:
        pos_maior.append(i+1)
    if v == menor:
        pos_menor.append(i+1)

print(f"O maior número é: {maior} e está nas posições {pos_maior}")
print(f"O menor número é: {menor} e está nas posições {pos_menor}")

n = []
while True:
    n.append(int(input("Digite um número: ")))
    if n[-1] in n[:-1]: #:-1 é para pegar o último número digitado, e n[:-1] é para pegar todos os números digitados, exceto o último
        print("Número já digitado, tente novamente.")
        n.pop()
    resposta = input("Quer continuar? [S/N] ").strip().upper()
    if resposta == "N":
        break
n.sort()
print(f"Você digitou os números: {n}")

n = []

for i in range(5):
    num = int(input("Digite um número: "))
    
    inserido = False
    
    for pos, val in enumerate(n):
        if num < val:
            n.insert(pos, num)
            inserido = True
            break
    
    if not inserido:
        n.append(num)

print(n)"""

"""
num5 = 0
n = []
while True:
    n.append(int(input("Digite um número: ")))
    resposta = input("Quer continuar? [S/N] ").strip().upper()
    if resposta in "N":
        break
print(f"foram digitados {len(n)} numeros)")
n.sort(reverse=True)
print(f"Os números em ordem decrescente são: {n}")
for i in n:
    if i == 5:
        num5 += 1
print(f"O número 5 foi digitado {num5} vezes.")"""
"""
n = []
while True:
    n.append(int(input("Digite um número: ")))
    resposta = input("Quer continuar? [S/N] ").strip().upper()
    if resposta in "N":
        break
impares = [i for i in n if i % 2 != 0]
pares = [i for i in n if i % 2 == 0]

print(f"Você digitou os números: {n}")
print(f"Os números pares digitados foram: {pares}")
print(f"Os números ímpares digitados foram: {impares}")"""

calculo = input("digite uma expressão: ")
pilha = []
for simb in calculo:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print('expressão valida')
else:
    print('expressão invalida')
