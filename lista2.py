"""
temp = []
princ = []
pesadas = []
leves = []

while True:
    temp.append(input('Digite seu nome: '))
    temp.append(float(input('Digite sua peso: ')))
    if temp[1] > 80:
        pesadas.append(temp[:])
    else:
        leves.append(temp[:])
    princ.append(temp[:])
    cadastros += 1
    temp.clear()

    resp = input('Deseja continuar? (S/N): ').upper().strip()
    if resp.upper() == 'N':
        break

print ('-=' * 30)

print(f'Foram cadastrados {len(princ)} pessoas.')
print(f'Pessoas pesadas: {len(pesadas)}')
print(f'Pessoas leves: {len(leves)}')
print ('-=' * 30)

print('Lista de pessoas pesadas:')
for p in pesadas:
    print(f'{p[0]} - {p[1]} kg')
print ('-=' * 30)

print('Lista de pessoas leves:')
for p in leves:
    print(f'{p[0]} - {p[1]} kg')
print ('-=' * 30)

num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')

somap = soma3c = mai2l = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            if c == 0:
                mai2l = matriz[l][c]
            elif matriz[l][c] > mai2l:
                mai2l = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores PARES é: {somap}')
print('-=' * 30)
print(f'A soma dos valores da 3ª coluna é: {soma3c}')
print('-=' * 30)
print(f'O maior valor da 2ª linha é: {mai2l}')

import random
from time import sleep
numeros = []
jogos = []
quantJ = int(input('Quantos jogos deseja fazer? '))
for j in range(quantJ):
    while len(numeros) < 6:
        numeros.append(random.randint(1, 60))
        if numeros.count(numeros[-1]) > 1:
            numeros.pop()
    jogos.append(numeros[:])
    numeros.clear()
print('-=' * 30)
print('SORTEANDO OS JOGOS'.center(60))
print('-=' * 30)
print('Os jogos sorteados foram:'.center(60))

for j in jogos:
    print(str(sorted(j)).center(60))
    sleep(1)
    """