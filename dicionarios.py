"""alunos = []

while True:
    dados = {
    'nome': input('Digite o nome do aluno: '),
    'idade': int(input('Digite a idade do aluno: ')),
    'nota': float(input('Digite a nota do aluno: ')),
    'aprovado': False
}
    if dados['nota'] >= 6.0:
        dados['aprovado'] = True
    else:       
        dados['aprovado'] = False

    alunos.append(dados.copy())

    continuar = input('Deseja cadastrar outro aluno? (s/n): ').lower()
    if continuar == 'n':
        break

print('os alunos cadastrados foram:')
for aluno in alunos:
    print(f"O aluno {aluno['nome']} tem {aluno['idade']} anos, nota {aluno['nota']} e a aprovação está: {aluno['aprovado']}")

import random
ranking = []
Jogadores = [
{
    'nome': 'jogador1',
    'pontuacao': random.randint(1, 6),
},
{
    'nome': 'jogador2',
    'pontuacao': random.randint(1, 6),
},
{
    'nome': 'jogador3',
    'pontuacao': random.randint(1, 6),
},
{
    'nome': 'jogador4',
    'pontuacao': random.randint(1, 6),
}
]

for jogador in Jogadores:
    print(f"O {jogador['nome']} tirou a pontuação de {jogador['pontuacao']}")
    if len(ranking) ==0:
        ranking.append(jogador)
    else:
        for i in range(len(ranking)):
            if jogador['pontuacao'] > ranking[i]['pontuacao']:
                ranking.insert(i, jogador)
                break
        else:
            ranking.append(jogador)
print('-='*20)
print('O ranking ficou:')

for i, jogador in enumerate(ranking, start=1):
    print(f"{i}. {jogador['nome']} - {jogador['pontuacao']}")

import datetime
pessoa = {
    'nome': input('Digite seu nome: '),
    'data_nascimento': int(input('Digite seu ano de nascimento: ')),
    'CTPS': int(input('Digite sua CTPS (0 se não tiver): ')),
}
pessoa['idade'] = datetime.datetime.now().year - pessoa['data_nascimento']

if pessoa['CTPS'] != 0:
    pessoa['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário: '))
    pessoa['aposentadoria'] = pessoa['ano_contratacao'] + 35 - pessoa['data_nascimento']
    print(f"{pessoa['nome']} de {pessoa['idade']} anos irá se aposentar aos {pessoa['aposentadoria']} anos.")
else:
    print (f"Olá {pessoa['nome']}, você tem {pessoa['idade']} anos.")"""

Jogador = {
    'nome': input('Digite o nome do jogador: '),
    'partidas': int(input('Digite o número de partidas jogadas: ')),
    'gol_total': 0,
    'gols_partida': []
}

for i in range(Jogador['partidas']):
    gols_partida = int(input(f'Quantos gols foram marcados na partida {i+1}? '))
    Jogador['gols_partida'].append(gols_partida)
    Jogador['gol_total'] += gols_partida

