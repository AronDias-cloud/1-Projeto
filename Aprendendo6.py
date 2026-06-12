import time
import random as rd
import math
import os
import json

'''
# Exercício 1 - Digite um número e mostre a largura e comprimento do terreno e a área do terreno, usando Função.
def area(comprimento, largura):
    print(f'A área do tamanho do terreno de {comprimento} x {largura} é: {comprimento * largura}m²')
comprimento = float(input('Digite o comprimento [m]: '))
largura = float(input('Digite a largura [m]: '))
area(comprimento, largura)
'''
'''
# Exercício 2 - Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
escreva('Olá, Mundo!')
escreva('Aprendendo Python no Youtube!')
'''
'''
# Exercício 3 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, 
# e realize a contagem, tendo uma contagem personalizada pela pessoa, e se o usuário não informar o passo, 
# ele deverá contar de 1 em 1.
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -1 * passo
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -1 * passo
    for i in range(inicio, fim + 1, passo):
        print(i, end=' ', flush=True)
        time.sleep(0.5)
    print('FIM!')
contador(1, 10, 1)
contador(10, 0, -2)
Inicio = int(input('Início: '))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))
contador(Inicio, Fim, Passo)
'''
'''
# Exercício 4 - Programa analisa os valores aplicados para a função, mostrando quantos números foram digitados
# e qual é o maior valor informado, se o valor mandado for nulo mostra que foi analisado (0)
def maior(*num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ', flush=True)
        time.sleep(0.5)
        if cont == 0:
            maior = v
        elif v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior()
'''
'''
# Exercício 5 - Programa que sorteia 5 números diferentes, e coloca numa lista, sendo usado numa outra função
# que vai somar os valores pares que estão na lista
def sorteia(lista):
    print('-=' * 20)
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = rd.randint(1, 10)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        time.sleep(0.5)
    print('\nSorteio finalizado!')
    somaPar(lista)
def somaPar(lista):
    print('Somando os valores pares de ', end='')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'{lista}', end='', flush=True)
    print(f' dar {soma}')
sorteia([])
'''
'''
# Assunto que aprendi e pode ser usado no futuro
print(input.__doc__)
help(input)
'''
'''
# Exercício 6 - Programa que vai ver a idade do usuário e manda para a função
# mostrando se o voto dele está negado/opcional/obrigatório
def voto(idade):
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
nascimento = (int(input('Em que ano você nasceu? ')))
idade = 2026 - nascimento
print(f'Com {idade} anos: {voto(idade)}')
'''
'''
# Exercício 7 - Programa que mostra a fatorial digitado pelo usuário e também mostra como foi feita a conta do usuário
# se o usuário querer que mostre o calculo feito
def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
num = int(input('Digite um número para calcular seu fatorial: '))
show = input('Deseja mostrar o processo de cálculo? [S/N] ').strip().upper()[0]
if show == 'S':
    show = True
    print('-='*20)
    print(fatorial(num, show=show))
else:
    show = False
    print('-='*20)
    print(f'O fatorial de {num} é {fatorial(num, show=show)}')
'''
'''
# Exercício 8 - Programa que usa a função para mostrar o Nome e números de Gols feitos.
# com condições que o nome e gols não fiquem vazios ou nulos
def ficha(nome='<desconhecido>', gols=0):
    print('-=' * 20)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
'''
'''
# Exercício 9 - Programa que faz o trabalho de fazer o input fazendo que o valor printado seja inteiro.
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        print('ERRO! Digite um número inteiro válido.')
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')
'''
'''
# Exercício 10 - Programa que pega o nome e as notas dos alunos, independente da quantidade de notas, e vai dizer
# a maior e menor nota, média das notas e a situação (opcional)
def notas(situacao=False):
    """
    => param situacao: Valor opcional para mostrar a situação do aluno.
    """
    turma = []
    while True:
        aluno = {}
        aluno['nome'] = input('Nome do aluno: ').strip()
        aluno['notas'] = [float(input(f'Notas de {aluno["nome"]}: '))]
        sit  = input('Deseja adicionar mais notas? [S/N] ').strip().upper()[0]
        while sit not in 'SN':
            sit = input('Resposta inválida. Deseja adicionar mais notas? [S/N] ').strip().upper()[0]
        while sit == 'S':
            aluno['notas'].append(float(input(f'Notas de {aluno["nome"]}: ')))
            sit = input('Deseja adicionar mais notas? [S/N] ').strip().upper()[0]
            while sit not in 'SN':
                sit = input('Resposta inválida. Deseja adicionar mais notas? [S/N] ').strip().upper()[0]
            while sit == 'N':
                break
        aluno['média'] = sum(aluno['notas']) / len(aluno['notas'])
        turma.append(aluno)
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    for s in turma:
        if s['média'] >= 7:
            s['situação'] = 'Aprovado'
        elif 5 <= s['média'] < 7:
            s['situação'] = 'Recuperação'
        else:
            s['situação'] = 'Reprovado'
    print('-=' * 10, end=' ')
    print(f'Boletim dos {len(turma)} alunos:', end=' ')
    print('-=' * 10)
    print()
    for a in turma:
        if situacao:
           print(f'O(A) aluno(a) {a["nome"]} teve a(s) {len(a["notas"])} nota(s): {a["notas"]}')
           print(f'Sendo o maior Nota: {max(a["notas"]):.1f} e a menor Nota: {min(a["notas"]):.1f}')
           print(f'Média: {a["média"]:.1f}')
           print(f'Situação: {a["situação"]}') 
           print('-=' * 20)
        else:
            print(f'O(A) aluno(a) {a["nome"]} teve a(s) {len(a["notas"])} nota(s): {a["notas"]}')
            print(f'Sendo o maior Nota: {max(a["notas"]):.1f} e a menor Nota: {min(a["notas"]):.1f}')
            print(f'Média: {a["média"]:.1f}')
            print('-=' * 20)
s = input('Deseja mostrar a situação dos alunos? [S/N] ').strip().upper()[0]
if s == 'S':
    situacao = True
elif s == 'N':
    situacao = False
notas(situacao=situacao)
'''
'''
# Exercício 11 - Criação do Sistema de Ajuda dos comandos do python. Só para quando digita (fim)
c = ('\033[m', '\033[1;37;42m', '\033[0;37;46m', '\033[1;30;47m', '\033[1;31;40m')
def ajuda(comando):
    funcao = eval(comando)
    doc = str(funcao.__doc__).strip()
    titulo(f'Acessando o manual do comando "{comando}"', cor=2)
    print(c[3], end='')
    for linha in doc.splitlines():
        print(linha)
    print(c[0], end='')
    time.sleep(2)
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0]) 
    time.sleep(1)
while True:
    comando = ''
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM' or comando.lower() == 'fim':
        titulo('Até logo!', 4)
        break
    else:
        ajuda(comando)
'''
'''
# Exercício 12 - Programa que faz um input usando função dentro de um módulo chamado dados, e que vai fazer um resumo
# contendo os valores colocados e calculados no módulo chamado moeda
import Aprendizado.moeda as moeda
import Aprendizado.dados as dados
Dinheiro = dados.leiaDinheiro
preço = Dinheiro('Digite o preço: R$')
moeda.resumo(preço, 80, 35)
'''
'''
# Exercício 13 - Programa que faz o uso do tratamento de exceções com as funções de input.
import Aprendizado.leiaIntFloat as leiaIntFloat
while True:
    try:
        n = leiaIntFloat.leiaInt('Digite um número inteiro: ')
    except (TypeError, ValueError):
        print('\033[1;31;40mERRO! Digite um número inteiro válido.\033[m')
    else:
        break
while True:
    try:
        r = leiaIntFloat.leiaFloat('Digite um número Real: ')
    except (TypeError, ValueError):
        print('\033[1;31;40mERRO! Digite um número real válido.\033[m')
    else:
        break
print(f'Valor inteiro digitado foi {n} e o real foi {r}')
'''
'''
# Exercício 14 - Aprendendo o uso de requests para ver se o python acessou ou não o site.
import requests
url = "https://www.pudim.com.br"
try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print(f"Sucesso! O Python acessou o site {url} corretamente.")
    else:
        print(f"O Python tentou acessar, mas o site retornou o status: {resposta.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao tentar acessar o site")
'''
'''
# Exercício 15 - Criação de um Pequeno Sistema para guardar informações do usuário (nome e idade), colocando em pratica
# tudo que aprendir anteriormente, e também usando o JSON e OS
import Aprendizado.leiaIntFloat as leiaIntFloat
import Aprendizado.PequenoSistema as PequenoSistema

dados = PequenoSistema.carregar_dados()
banco_dados = dados

while True:
    PequenoSistema.titulo('MENU PRINCIPAL')
    PequenoSistema.opção1('1', 5)
    PequenoSistema.opção('Ver pessoas cadastradas ', 3)
    PequenoSistema.opção1('2', 5)
    PequenoSistema.opção('Cadastrar nova Pessoa ', 3)
    PequenoSistema.opção1('3', 5)
    PequenoSistema.opção('Sair do Sistema ', 3)
    print('='*40)
    
    try:
        opc = leiaIntFloat.leiaint('\033[0;33mSua Opção: \033[m')
        if opc > 3:
            print('\033[1;31;40mERRO! Digite uma opção entre 1 à 3\033[m')
    except (TypeError, ValueError):
            print('\033[1;31;40mERRO! Digite uma opção correta\033[m')
    except KeyboardInterrupt:
            print('\033[1;31;40mERRO! O usuário não quis informar os dados\033[m')
            break    
    else:
        if opc == 1:
            PequenoSistema.titulo('PESSOAS CADASTRADAS')
            PequenoSistema.lista(banco_dados)
        elif opc == 2:
            PequenoSistema.titulo('NOVO CADASTRO')
            novo_usuario = PequenoSistema.cadastro()
            if novo_usuario:
                banco_dados.append(novo_usuario)   
                PequenoSistema.salvar_dados(banco_dados)     
        elif opc == 3:
            PequenoSistema.titulo('Saindo do sistema... Até logo!')
            time.sleep(0.2)
            break
'''