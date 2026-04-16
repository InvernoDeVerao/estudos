from funcoes import *
from cores import *
from arquivo.pessoas import arquivoexiste, criararquivo, lerarquivo, criarpessoa

arq = 'pessoas.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    opcao = menu(['Ver lista de pessoas', 'Cadastrar pessoa', 'Sair'])
    if opcao == 1:
        lerarquivo(arq)
    elif opcao == 2:
        criarpessoa(arq, nome=input("Nome: "), idade=leia_int("Idade: "))
    elif opcao == 3:
        break
    else:
        cabeçalho(VERMELHO + "Opção inválida! Tente novamente." + RESET)
