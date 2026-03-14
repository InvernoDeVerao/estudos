"""soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 999:
        break
    soma += n
    quantidade += 1

print(f"Você digitou {quantidade} de números.")
print(f"A soma dos números digitados é: {soma}")

while True:
    t = int(input("Digite o numero que deseja saber a tabuada: "))
    if t < 0:
        print("Número negativo, programa encerrado.")
        break
    print(f"Tabuada de {t}:")
    for i in range(1, 11):
        print(f"{t} x {i} = {t * i}")

from random import randint

v = 0
while True:
    escolha = int(input("Digite 1 para impar e 2 para par: "))
    if escolha not in [1, 2]:
        print("\nOpção inválida. Tente novamente.")
        continue
    numero = randint(1, 10)
    numeroPlayer = int(input("Digite um número de 1 a 10: "))
    if numeroPlayer < 1 or numeroPlayer > 10:
        print("\nNúmero inválido. Tente novamente.")
        continue
    soma = numero + numeroPlayer
    if (soma % 2 == 0 and escolha == 2) or (soma % 2 != 0 and escolha == 1):
        print(f"\nVocê venceu! O número sorteado foi {numero} e a soma é {soma}.")
        v += 1
    else:
        print(f"\nVocê perdeu! O número sorteado foi {numero} e a soma é {soma}.")
        break
    print(f"\nVocê teve {v} vitórias consecutivas.")"""

M = 0
F = 0
idade = 0
maior = 0
mjovem = 0
contador = 0
while True:
    sexo = str(input("\nDigite seu sexo [M/F]: ")).strip().upper()[0]
    if sexo not in ['M', 'F']:
        print("\nOpção inválida. Tente novamente.")
        continue
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("\nIdade inválida. Tente novamente.")
        continue
    print(f"\nSexo {sexo} registrado com sucesso.")
    print(f"Idade {idade} registrada com sucesso.")
    if idade >= 18:
        print("\nVocê é maior de idade.")
        maior += 1
    if sexo == 'M':
        M += 1
    else:
        F += 1
        if idade < 20:
            print("\nVocê é uma mulher jovem.")
            mjovem += 1
    contador = int(input("\nDigite 1 para continuar ou 2 para encerrar: "))
    if contador == 2:
        print(f"\nTotal de homens registrados: {M}")
        print(f"Total de mulheres registradas: {F}")
        print(f"Total de pessoas maiores de idade: {maior}")
        print(f"Total de mulheres jovens: {mjovem}")
        print("Encerrando o programa.")
        break
    elif contador != 1:
        print("Opção inválida. Tente novamente.")
        