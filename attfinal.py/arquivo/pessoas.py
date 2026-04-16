from funcoes import *
from cores import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(VERMELHO + "Houve um erro na criação do arquivo!" + RESET)
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(VERMELHO + "Erro ao ler o arquivo!" + RESET)
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        print(AZUL + a.read() + RESET)
        a.close()

def criarpessoa(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print(VERMELHO + "Houve um erro na abertura do arquivo!" + RESET)
    else:
        a.write(f"{nome};{idade}\n")
        a.close()