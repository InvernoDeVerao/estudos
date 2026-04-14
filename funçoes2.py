"""from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Você com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Você com {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


def fatorial(num, show=False):
    f = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
    return f


num1 = int(input('Digite um número para calcular seu fatorial: '))
show1 = input('Deseja mostrar o processo? [S/N] ').strip().upper()[0]
if show1 == 'S':
    show1 = True
else: 
    show1 = False

print(fatorial(num1, show=show1))

def ficha(jogador='<desconhecido>', gols=0):
    print('=-' * 20)
    if jogador == '':
        jogador = '<desconecido>'
    if gols == '':
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols == '':
    gols = 0
else:
    gols = int(gols)

print(ficha(nome, gols))"""

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        m = input(msg)
        if m.isnumeric():
            valor = int(msg)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {n}.')