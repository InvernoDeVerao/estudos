"""def tamanho(a, b):
    t = a*b
    return f'A area do terreno {a}x{b} é de {t}m²'


print(tamanho(10, 20))


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Olá, Mundo!')
escreva('Python é incrível!')
escreva('Funções são muito úteis!')


from time import sleep

def contador(i, f ,p):
    print('=-' * 20)
    if p < 0:
             p *= -1
    elif p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        sleep(2)
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        sleep(2)
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)


def maior(*num):
    print ('-=' * 30)
    if len(num) == 0:
        return 'Nenhum valor informado.'
    maior = num[0]
    print(f'Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        if n > maior:
            maior = n
    return f'\nO maior valor informado foi {maior}'

print(maior(2, 9, 4, 5, 7, 1))
print(maior(4, 7, 0))
print(maior())


from random import randint
numeros = []
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 100)
        lst.append(n)
        print(n, end=' ')
    print('PRONTO!')

def somaPar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {lst}, temos {s}')


sorteia(numeros)
somaPar(numeros)
"""

