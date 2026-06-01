import math
import random as rd
import time

'''
# Exercício 1 - Programa que diz, qual o maior e menor valor de uma lista e suas posições
valores = []
for i in range(1, 6):
    num  = int(input(f'Digite o {i}º número: '))
    valores.append(num)
    min_val = min(valores)
    max_val = max(valores)
    pos_min = []
    pos_max = []
    for pos, num in enumerate(valores):
        if num == min_val:
            pos_min.append(pos)
        if num == max_val:
            pos_max.append(pos)
print(f'Esses são os valores: {valores}')
print(f'Sendo o menor valor o {min_val} que está na posição {pos_min}')
print(f'Sendo o maior valor o {max_val} que está na posição {pos_max}')
'''
'''
# Exercício 2 - Programa que faz que cada valor seja adicionado uma unica vez
# e deixe de forma organizada e crescente.
valores = []
while True:
        num = int(input('Digite vários números diferentes: '))
        if num not in valores:
            valores.append(num)
            print('Valor adicionado com sucesso')
        else:
            print('Valor Duplicado! Não adicionado')
        usuario = input('Quer continuar? [S/N]').upper().strip()
        if usuario == 'N':
            break
valores = sorted(valores)
print(valores)
'''
'''
# Exercício 3 - Programa que faz o uso do (sort) sem usar ele, mostrando a posição de cada um na lista
valores = []
for _ in range(1, 6):
    usuario = int(input('Digite um valor: '))
    pos = 0
    while pos < len(valores) and valores[pos] < usuario:
        pos += 1
    valores.insert(pos, usuario)
    print(f'Adicionado na posição {pos} da lista...')
print(f'Esses são os números digitados {valores}')
'''
'''
# Exercício 4 - Programa que mostra quantos números foram digitados, a lista em forma decrescente, 
# e se o valor [5] está ou não na lista.
valores = []
while True:
    num = int(input('Digite um número:'))
    usuário = input('Quer continuar? [S/N] ').upper()
    valores.append(num)
    valor = len(valores)
    if 5 in valores:
        val = ('Sim')
    else:
       val = ('Não')
    if usuário == 'N':
        break
print(valores)
print(f'Quantos números foram digitados? {valor}')
valores.sort(reverse=True)
print(f'A lista [valores] em forma descrescente é: {valores}')
print(f'O valor [5] está na lista? {val}')
'''
'''
# Exercício 5 - Programa que mostra os números digitados e que separa os números pares e impares em listas diferentes, 
# mostrando o resultado no final.
valores = []
val_par = []
val_impar = []
while True:
    num = int(input('Digite um número:'))
    usuário = input('Quer continuar? [S/N] ').upper()
    valores.append(num)
    if num % 2 == 0:
        val_par.append(num)
    else:
        val_impar.append(num)
    if usuário == 'N':
        break
print(f'Os valores digitados: {valores}')
print(f'Os valores pares da lista [valores]: {val_par}')
print(f'Os valores impares da lista [valores]: {val_impar}')
'''
'''
# Exercício 6 - Programa que mostra se a expressão digitada pelo usuário está correta ou não, ou seja, 
# se os parênteses estão fechados ou não.
while True:
    usuario = str(input('Digite uma expressão: '))
    paren = []
    par_esquerda = paren.count('(')
    par_direita = paren.count(')')
    if par_direita == par_esquerda:
        print('A expressão está certa')
        break
    else:    
        print('A expressão está errada')
'''
'''
# Exercício 7 - Programa que mostra o nome e o peso de várias pessoas, mostrando quantas pessoas foram cadastradas, 
# quem é a pessoa mais pesada e quem é a mais leve.
inf = []
inf2 = []
peso = 0
nome = []
nome1 = []
while True:
    inf.append(str(input('Nome: ')))
    inf.append(float(input('Peso: ')))
    usuario = input('Quer continuar? [s/n] ').lower()
    inf2.append(inf[:])
    inf.clear()
    if usuario == 'n':
        break
quant = len(inf2)
peso = inf2[0][1] + 1
for i in range(0, len(inf2)):
    if inf2[i][1] >= peso:
        peso = inf2[i][1]
        nome.append(inf2[i][0])
    else:
        peso1 = inf2[i][1]
        nome1.append(inf2[i][0])
print(f'A quantidade de pessoas cadastradas na lista é {quant}')
print(f'A pessoa mais pesada é {nome} pesando {peso}')
print(f'A pessoa mais leve é {nome1} pesando {peso1}')
'''
'''
# Exercício 8 - Programa que mostra os números digitados e que separa os números pares e impares em listas diferentes, 
# mostrando o resultado no final, e deixando as listas organizadas de forma crescente.
inf = []
inf2 = []
inf3 = []
num = []
num1 = []
for i in range(7):
    inf.append(int(input(f'Digite o {i}º número: ')))
    inf2.append(inf[i])
    inf3.append(inf2[:])
    inf2.clear()
for i in range(0, len(inf3)):
    if inf3[i][0] % 2 == 0:
        num.append(inf3[i][0])
    else:
        num1.append(inf3[i][0])
num = sorted(num)
num1 = sorted(num1)
print(inf3)
print(f'Pares: {num}')
print(f'Impares: {num1}')
'''
'''
# Exercício 9 - Programa que mostra os números digitados em forma de matriz, mostrando a soma dos valores pares, 
# a soma dos valores da 3º coluna, e o maior valor da 2º coluna, usando uma lista dentro de outra lista.
inf = []
inf2 = []
soma = 0
for i in range(0, 3):
    for j in range(0, 3):
        inf.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if len(inf) == 3:
            inf2.append(inf[:])
            inf.clear()
print("\n---- Resultado Final ----")
for linha in inf2:
    for valor in linha:
        print(f'  [ {valor} ]', end=' ')
    print()
print('-='*30)
seg_max = max(inf2[1])
for lis in inf2:
    som = sum(lis)
    for num in lis:
        if num % 2 == 0:
                soma += num        
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma de todos os valores da 3º coluna é: {som}')
print(f'O maior valor da 2º coluna é: {seg_max}')
'''
'''
# Exercício 10 - Programa que mostra os números sorteados para a mega sena, mostrando 
# quantos jogos o usuário quer que sejam sorteados, e mostrando os números sorteados de cada jogo.
inf = []
inf2 = []
usuario = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, end='  ')
print(f'SORTEANDO {usuario} JOGOS', end='  ')
print('-='*3)
for i in range(1, usuario + 1):    
    inf.append(rd.sample(range(1, 60), k=6))
    for linha in inf:
        time.sleep(1)
        print(f'Jogo {i}: {linha} ')
    inf.clear()
'''
'''
# Exercício 11 - Programa que mostra o nome, as notas e a média de várias pessoas, 
# mostrando no final um boletim com a média de cada um, e dando a opção de mostrar as notas de cada aluno individualmente.
Aluno = []
notas = []
num = []
while True:
    Aluno.append(str(input('Nome: ')))
    Aluno.append(int(input('Nota 1: ')))
    Aluno.append(int(input('Nota 2: ')))
    usuario = input('Você quer continuar [s/n]? ').lower()
    notas.append(Aluno[:])
    Aluno.clear()
    if usuario == 'n':
        break
print('-='*5, end='')
print(' BOLETIM ', end='')
print('-='*5)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>6}')
print('-'*20)
for i in range(0, len(notas)):
    média = (notas[i][1]+notas[i][2]) / 2
    nome = notas[i][0]
    print(f'{i:<4}{nome:<12}{média:>6.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
            print('FINALIZANDO...')
            time.sleep(1.2)
            print('---VOLTE SEMPRE---')
            break
    num.append(opc)
    for i in num:
            nome = notas[i][0]
            nota1 = notas[i][1]
            nota2 = notas[i][2]
            print(f'Notas de {nome} são [{nota1}, {nota2}]')
            num.clear()
'''
'''
# Exercício 12 - Programa que mostra o nome, a média e a situação de um aluno, mostrando se ele passou ou não, 
# sabendo que a média para passar é 7 usando dicionario --> {}
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
for k, v in aluno.items():
    print(f'{k} é {v}')
if aluno['Média'] >= 7:
    print('Você passou')
else:
    print('Você não passou')
'''
'''
# Exercício 13 - Programa que mostra o nome e o resultado de um jogo de dados, mostrando o ranking do jogo, ou seja, 
# quem ganhou, quem ficou em segundo, terceiro e quarto lugar usando dicionário e time.
jogadores = {}
jogo = []
ranking= []
posicao = 1
for _ in range(0, 4):
    jogadores['jogador'] = str(input('Nome: '))
    sorte =  rd.sample(range(1, 7), 1)[0]
    jogadores['resultado'] = sorte
    jogo.append(jogadores.copy())
for jg in jogo:
    for k, v in jg.items():
        time.sleep(0.5)
        print(f'{k}: {v}', end=' ')
        print()
while len(jogo) > 0:
    maior_jogador = jogo[0]
    for jg in jogo:
        if jg['resultado'] > maior_jogador['resultado']:
            maior_jogador = jg
    ranking.append(maior_jogador)
    jogo.remove(maior_jogador)
for jg in ranking:
    time.sleep(0.5)
    print(f'{posicao}º Lugar: {jg["jogador"]} com o número {jg["resultado"]}')
    posicao = posicao + 1
'''
'''
# Exercício 14 - Programa que mostra o nome, a idade, a carteira de trabalho e o salário de um trabalhador, 
# mostrando se ele tem ou não carteira de trabalho, e se tiver, mostrando o dicionário chamado (clt) e 
# quantos anos faltam para ele se aposentar, sabendo que a aposentadoria é com 35 anos de contribuição.
clt = {}
l = []
clt['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
clt['Idade'] = 2026 - ano
clt['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if clt['CTPS'] != 0:
    clt['Contratação'] = int(input('Ano de contratação: '))
    cont = (clt['Contratação'] + 35) - ano
    clt['Salário'] = float(input('Salário: R$'))
    clt['Aposentadoria'] = cont
    l.append(clt.copy())
else:
    l.append(clt.copy())
print('-='*20)
for c in l:
    for k, v in c.items():
        time.sleep(0.5)
        print(f'{k}: {v}', end=' ')
        print()
'''
'''
# Exercício 15 - Programa que mostra o nome, a quantidade de partidas jogadas, 
# os gols feitos em cada partida e o total de gols feitos por um jogador, mostrando no final um resumo do desempenho.
jogador = {}
jogo = []
g = []
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas Jogadas'] = int(input('Quantidade de partidas jogadas: '))
for p in range(1, jogador['Partidas Jogadas']+1):
    g.append(int(input(f'Gols em cada partida {p}: ')))
jogador['Gol em cada Partida'] = g
jogador['Total de Gols']= sum(g)
jogo.append(jogador.copy())
print('-='*30)
for c in jogo:
    print(c)
    print('-='*30)
    for k, v in c.items():
        time.sleep(0.5)
        print(f'{k}: {v}', end=' ')
        print()
print('-='*30)
for c in jogo:
    time.sleep(0.5)
    print(f'O jogador {c['Nome']} jogou {c['Partidas Jogadas']} partidas')
    for p in range(0, c['Partidas Jogadas']):
        time.sleep(0.5)
        g = c['Gol em cada Partida']
        print(f'    => Na partida {p}, fez {g[p]} gols')
    print(f'Foi um total de {c['Total de Gols']} gols')
'''
'''
# Exercício 16 - Programa que mostra o nome, a idade e o sexo de várias pessoas, mostrando quantas pessoas foram cadastradas, 
# a média de idade do grupo, uma lista com as mulheres do grupo e uma lista com as pessoas que estão acima da média de idade.
inf = {}
inf2 = []
soma = 0
nome_f = []
inform = []
while True:
    inf['Nome'] = str(input('Nome: ')).strip()
    ano = int(input('Ano de Nascimento: '))
    inf['Idade'] = 2026 - ano
    inf['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    inf2.append(inf.copy())
    usuario = input('Quer continuar? [s/n] ').lower()
    if usuario == 'n':
        break
num = len(inf2)
for i in inf2:
    soma += i['Idade']
    media = soma / num
time.sleep(0.5)
print(f'- O grupo tem {num} pessoa')
for i in inf2:
    if i['Sexo'] == 'F':
        nome_f.append(i['Nome'])
    if i['Idade'] > media:
        inform.append(i)
time.sleep(0.8)
print('-='*30)
print(f'- A média da idade das pessoas é {media} anos')
print('-='*30)
print(f'- As mulheres no grupo são: ', end='') 
for i in range(0, len(nome_f)):
    time.sleep(0.8)
    print(f'{nome_f[i]}', end=', ')
print()
print('-='*30)
print(f'- A Lista das pessoas que estão acima da média:')
print()
for i in inform:
    for k, v in i.items():
        time.sleep(0.8)
        print(f'{k}: {v}')
'''
'''
# Exercício 17 - Programa que segue a mesma questão 15, mas mostrando o desempenho de vários jogadores, 
# e dando a opção de mostrar o desempenho individual de cada jogador.
jogador = {}
jogo = []
while True:
    g = []
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas Jogadas'] = int(input('Quantidade de partidas jogadas: '))
    for p in range(1, jogador['Partidas Jogadas']+1): 
        g.append(int(input(f'Gols em cada partida {p}: ')))
    jogador['Gol em cada Partida'] = g.copy()
    jogador['Total de Gols']= sum(g)
    jogo.append(jogador.copy())
    usuario = input('Quer continuar? [s/n] ').lower()
    if usuario == 'n':
        break
for c in jogo:
    print('-='*15, end='')
    print(f' JOGADOR ', end='')
    print('-='*15)
    for k, v in c.items():
        time.sleep(0.5)
        print(f'{k}: {v}', end=' ')
        print()
print('-='*34)
while True:
        print('-' * 40)
        print(f"{'Cod':<5}{'Nome':<15}{'Total Gols':<10}")
        print('-' * 40)
        for i, c in enumerate(jogo):
            print(f"{i:<5}{c['Nome']:<15}{c['Total de Gols']:<10}")
        print('-' * 40)
        opc = int(input('Mostrar os dados de qual jogador? (999 para parar): '))
        if opc == 999:
            print('<< VOLTE SEMPRE >>')
            break
        if opc >= len(jogo) or opc < 0:
            print(f'ERRO! Não existe jogador com código {opc}! Tente novamente.')
        else:
            jogador_ = jogo[opc]
            print(f"\n -- LEVANTAMENTO DO JOGADOR {jogador_['Nome']}:")
            for partida in range(0, jogador_['Partidas Jogadas']):
                time.sleep(0.5)
                gols_lista = jogador_['Gol em cada Partida']
                print(f'    => Na partida {partida + 1}, fez {gols_lista[partida]} gols.')
            print(f"Foi um total de {jogador_['Total de Gols']} gols.\n")
'''