def dobro(x=0, formatado=True):
    resultado = x * 2
    if formatado:
        return moeda(resultado)
    return resultado

def metade(x=0, formatado=True):
    resultado = x / 2
    if formatado:
        return moeda(resultado)
    return resultado

def aumentar(x=0, p=20, formatado=True):
    """
    Aumenta o valor de x em p porcento.
    """
    resultado = x + (x * p / 100)
    if formatado:
        return moeda(resultado)
    return resultado

def diminuir(x=0, p=20, formatado=True):
    """
    Diminui o valor de x em p porcento.
    """
    resultado = x - (x * p / 100)
    if formatado:
        return moeda(resultado)
    return resultado

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.')
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print(f'\033[0;31mERRO! "{valor}" é um preço inválido.\033[m')

def resumo(preco=0, por=0):
    print('-=' * 20)
    print('RESUMO DOS VALORES'.center(40))
    print('-=' * 20)
    print(f'Preço: {moeda(preco)}')
    print(f'Dobro: {dobro(preco, formatado=True)}')
    print(f'Metade: {metade(preco, formatado=True)}')
    print(f'Aumento de {por}%: {aumentar(preco, por, formatado=True)}')
    print(f'Diminuição de {por}%: {diminuir(preco, por, formatado=True)}')
    print('-=' * 20)