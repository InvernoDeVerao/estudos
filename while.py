"""genero = str(input("digite seu genero [M/F]: ")).strip().lower()

while genero not in ['m', 'f']:
    genero = str(input("digite seu genero [M/F]: ")).strip().lower()
if genero == "m":
    print("Olá, senhor!")
elif genero == "f":
    print("Olá, senhora!")


contador = 0
while contador != 5:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print("Digite 1 para somar, 2 para subtrair, 3 para multiplicar, 4 para dividir e 5 para sair")
    contador = int(input("Digite oq quer fazer: "))
    if contador == 1:
        print(f"A soma de {n1} + {n2} é igual a {n1 + n2}")
    elif contador == 2:
        print(f"A subtração de {n1} - {n2} é igual a {n1 - n2}")
    elif contador == 3:
        print(f"A multiplicação de {n1} * {n2} é igual a {n1 * n2}")
    elif contador == 4:
        if n2 != 0:
            print(f"A divisão de {n1} / {n2} é igual a {n1 / n2}")
        else:
            print("Não é possível dividir por zero.")
    elif contador == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")

n = int(input("Digite um número para saber seu fatorial: "))
fatorial = 1
contador = n
while contador > 1:
    fatorial *= contador
    contador -= 1
print(f"O fatorial de {n} é {fatorial}")

numero = int(input("Digite um número: "))
fi1 = 0
fi2 = 1

while numero < 0:
    print("Número inválido. Digite um número positivo.")
    numero = int(input("Digite um número: "))
for i in range(numero):
    print(fi1)
    fi1, fi2 = fi2, fi1 + fi2
"""
