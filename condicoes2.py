"""salario = int(input("Digite o seu salário: "))
vCasa = int(input("Digite o valor da casa: "))
anos = int(input("Digite o número de anos para pagar a casa: "))

prestacao = vCasa / (anos * 12)

if prestacao <= salario * 0.3:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")

n1 = int(input("Digite o primeiro número: "))
conversao = int(input("Digite a conversão desejada Binario (1) ou Octal (2) hexadecimal (3): "))

if conversao == 1:
    print(f"O número {n1} em binário é: {bin(n1)[2:]}")#bin = função para converter um número inteiro em binário, o [2:] é para remover os dois primeiros caracteres "0b" que indicam que é um número binário.
elif conversao == 2:
    print(f"O número {n1} em octal é: {oct(n1)[2:]}")#oct = função para converter um número inteiro em octal, o [2:] é para remover os dois primeiros caracteres "0o" que indicam que é um número octal.
elif conversao == 3:
    print(f"O número {n1} em hexadecimal é: {hex(n1)[2:]}")#hex = função para converter um número inteiro em hexadecimal, o [2:] é para remover os dois primeiros caracteres "0x" que indicam que é um número hexadecimal.
else:
    print("Opção de conversão inválida.")
"""
import random

resultado = 0
for i in range(1, 4):
    Mjoken = (random.randint(1, 3))
    Jjoken = int(input("Digite 1 para Pedra, 2 para Papel e 3 para Tesoura: "))
    if Jjoken == Mjoken:
        print("Empate!")
    elif (Jjoken == 1 and Mjoken == 3) or (Jjoken == 2 and Mjoken == 1) or (Jjoken == 3 and Mjoken == 2):
        print("Você venceu!")
        resultado += 1
    else:
        print("Você perdeu!")
        resultado -= 1
if resultado > 0:
    print("Parabéns! Você ganhou o jogo!")
elif resultado < 0:
    print("Que pena! Você perdeu o jogo!")
else:
    print("O jogo terminou empatado!")

