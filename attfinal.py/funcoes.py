from cores import *

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print(VERMELHO + "Erro! Digite um número inteiro válido." + RESET)

def linha(tamanho=42):
    return '-' * tamanho

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabeçalho(AMARELO + "MENU PRINCIPAL" + RESET)
    for i, item in enumerate(lista):
        print(f"{VERDE}{i+1}{RESET} - {AZUL}{item}{RESET}")
    print(linha())
    opc = leia_int(VERDE + "Sua opção: " + RESET)
    return opc