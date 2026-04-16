from funcoes import *
from cores import *

while True:
    opcao = menu(['Ver lista de pessoas', 'Cadastrar pessoa', 'Sair'])
    if opcao == 1:
        cabeçalho("Opção 1: Ver lista de pessoas")
    elif opcao == 2:
        cabeçalho("Opção 2: Cadastrar pessoa")
    elif opcao == 3:
        cabeçalho(AMARELO + "Saindo do programa..." + RESET)
        break
    else:
        cabeçalho(VERMELHO + "Opção inválida! Tente novamente." + RESET)