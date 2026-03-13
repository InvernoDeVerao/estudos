
import random

numero = random.randint(1, 10)
print("Tente adivinhar o número entre 1 e 10 em 3 chances:")

for i in range(3):
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero:
        break
    if palpite < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")

if palpite == numero:
    print("Parabéns! Você acertou o número.")
else:
    print(f"Que pena! O número era {numero}.")

Velocidade = float(input("Digite a velocidade do carro em km/h: "))
if Velocidade > 80:
    print("Multa! Você ultrapassou o limite de velocidade.")
else:    
    print("Velocidade dentro do limite. Dirija com segurança!")   

if Velocidade > 80:
    multa = (Velocidade - 80) * 7
    print(f"A multa é de R$ {multa:.2f}.")


numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:    
    print("O número é ímpar.")

Km = float(input("Digite a distância em km: "))
passagem = 0
if Km < 0:
    print("Distância inválida. Por favor, digite um valor positivo.")
elif Km <= 200:
    print("A passagem custa R$ 0,50 por km.")
    passagem = Km * 0.50
else:
    print("A passagem custa R$ 0,45 por km.")
    passagem = Km * 0.45

print(f"O valor da passagem é R$ {passagem:.2f}.")
