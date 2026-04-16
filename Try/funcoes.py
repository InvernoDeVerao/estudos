def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print("Erro! Digite um número inteiro válido.")

def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except (ValueError, TypeError):
            print("Erro! Digite um número real válido.")