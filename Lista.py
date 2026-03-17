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
print(f"Você digitou os números: {n}")"""

n = []
for i in range(5):
    n.append(int(input("Digite um número: ")))
    if n 

