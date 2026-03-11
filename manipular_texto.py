nome = input("Digite seu nome e sobrenome: ")
print(nome.replace(" ", ""))#remove os espaços
print(nome.upper())#maiusculo
print(nome.lower())#minusculo
print(nome.title())#primeira letra maiuscula
print(nome.strip())#remove espaços no inicio e no final
print(nome.lstrip())#remove espaços no inicio
print(nome.rstrip())#remove espaços no final
print(nome.split())#separa as palavras em uma lista
print(nome.split()[0])#acessa a primeira palavra da lista
print(nome.split()[1])#acessa a segunda palavra da lista
print(nome.replace("a", "o"))#substitui a letra a por o
print(nome.find("a"))#encontra a posição da letra a
print(nome.count("a"))#conta quantas vezes a letra a aparece

print(nome.split())
primera_palavra = nome.split()[0]
print(len(primera_palavra))#conta quantas letras tem a primeira palavra