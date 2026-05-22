import math
import random as rd
import time

'''
# Exercício 1 - Qual o sexo da pessoa!

sexo = ''.upper()
sexo1 = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Coloque o seu sexo: ').upper()
    if sexo == 'M' or sexo == 'F':
     if sexo == 'F':
        sexo1 = 'Feminino'
     elif sexo == 'M':
        sexo1 = 'Masculino'
print(f'O seu sexo é {sexo1}')
'''
'''
# Exercício 2 - Escolha qual a opção que queres para calcular

valores = int(input('Digite um número: '))
valores1 = int(input('Digite um número: '))
menu = int(input('Digite qual a sua opção [1 a 5]? '))
total = 0
while menu != 0:
    if menu == 1:
        total = valores + valores1
        menu = 0
    elif menu == 2:
        total = valores * valores1
        menu = 0
    elif menu == 3:
         total = max(valores, valores1)
         menu = 0
    elif menu == 4:
       valores = int(input('Digite um número: '))
       valores1 = int(input('Digite um número: '))
       menu = int(input('Digite qual a sua opção? '))
    elif menu == 5:
        print('Você saiu do programa')
        menu = 0
print(f'O valor total escolhido por você é {total}')        
'''
'''
# Exercício 3 - Fazendo uma fatorial usando While

num = int(input('Digite um número: '))
total = 1
num1 = num
while num > 1:
    total = total * num
    print(total)
    num -= 1
print(f'A fatorial de {num1} é {total}')
'''
'''
#Exercício 4 - Fazendo uma PA usando While

usuario = ''
a = int(input('Digite o mesmo que o primeiro termo: '))
b = 0
primeiro = int(input('Digite um termo: '))
decimal1 = 0
razao = int(input('Digite uma razão: '))
decimal = primeiro + (10 - 1) * razao
while a > b:
    usuario = input(f'Você quer mais termos [s/n]? ').lower().strip()
    if usuario == 'n':
       print('Receba os seus termos')
       for i in range(primeiro, decimal + razao, razao):
            print([i])
            a -= 1
    elif usuario == 's':
       decimal1 = int(input('Quantos queres? '))
       decimal = decimal + decimal1 * razao
'''
'''
#Exercício 5 - Sequência de Fibonacci (Tive ajuda do Guanabara para corrigir)

num = int(input('Digite quantas repetições você quer: '))
n = 0
b = 1
print(f'{n} -> {b}', end='')
cont = 3
while cont <= num:
    a = n + b
    print(f' -> {a}', end= '')
    n = b
    b = a
    cont += 1
#Se quiser fazer de forma simplicada (n, b = b, n + b) 
'''
'''
#Exercício 6 - Uso do While para ver quantos números digitados e a soma delas
#vendo sempre se o número der 999 (Se der 999, o codigo dar um break)

numero = 0
num = []
while numero < 999:
    numero = int(input('Digite os números até 998: '))
    num.append(numero)
    quantos_numeros = len(num)
    soma_numeros = sum(num)
print(f"""A quantidade de números que você digitou foi {quantos_numeros}
e a soma desses mesmos números são {soma_numeros}""")
print(num)
'''
'''
#Exercício 7 - Programa que faz o usuário digitar varios números, enquanto, o usuário quiser digitar.
#quando o usuário não quiser mais digitar, mostra os seus valores (max, min e a média).

usuario = ''
numeros = 0
num = []
while usuario != 'n':
    numeros = int(input('Digite algum número: '))
    num.append(numeros)
    num_media = sum(num) / len(num)
    num_max = max(num)
    num_min = min(num)
    usuario = input('Você quer continuar a digitar números? [s/n]').lower().strip()
print(f"""O maior valor é {num_max} e o menor valor é {num_min}
    e a media dos valores é {num_media}""")   
'''
'''
#Exercício 8 - Programa que faz um usuário digitar varios números, 
#enquanto ele não digitar o número 999, os números digitados são acumulados numa lista e somam eles.

num = 0
n = []
s = 0
while num < 1000:
    num = (int(input('Digite um número: ')))
    if num != 999:
        n.append(num)
    elif num == 999:
        break
    s += num
n = len(n)
print(f'A quantidade de números digitados é {n}')
print(f'A soma dos números é {s}') 
'''
'''
#Exercício 9 - Tabuada usando While, podendo usar várias vezes até dizer um número negativo

num = 1
while num >= 0:
    num = int(input('Digite um número:'))
    if num < 0:
        break
    elif num >= 0:
         for i in range(1, 11):
            print(f'{num} * {i} = {num * i}')
'''
'''
#Exercício 10 - Jogo do PAR e IMPAR

Pc = rd.randint(1, 10)
vitorias = 0
while True:
    usuario = int(input('Digite um valor de 1 até 10: '))
    jogo = input('Você quer PAR ou ÍMPAR? [P/I]').upper()
    soma = usuario + Pc
    print(f'Você jogou {usuario} e o computador {Pc}. ', end='')
    if jogo == 'P':
        print(f'Total de {soma} DEU PAR ')
    if jogo == 'I':
        print(f'Total de {soma} DEU ÍMPAR ')
    if soma % 2 == 0 and jogo == 'P':
        print('VOCÊ VENCEU!!') 
        print('Vamos jogar novamente...') 
        vitorias += 1
    elif soma % 2 == 1 and jogo == 'I':
        print('VOCÊ VENCEU!!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('VOCÊ PERDEU!! \n')
        break
print(f'A quantidade de vitórias feitas no jogo foi {vitorias}')
'''
'''
Exercício 11 - Programa que ver a idade e sexo, respondendo alguns quesitos:

quant_idade = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Qual a sua Idade? '))
    sexo = input('Qual seu sexo? [F/M] ').upper()
#A) Quantas pessoas tem mais de 18 anos?
    if idade > 18:
         quant_idade += 1
#B) Quantas pessoas são homens?
    if sexo == 'M':
         homens += 1
#C) Quantas pessoas são mulheres que tem menos de 20 anos?
    elif sexo == 'F' and idade < 20:
         mulheres += 1
    usuário = input('Você quer continuar? [s/n]').lower()
    if usuário == 'n':
         break    
print(f'A {quant_idade} pessoa tem mais de 18 anos')
print(f'A {homens} pessoas são homens')
print(f'A {mulheres} pessoas são mulheres que tem menos de 20 anos')
'''
'''
#Exercício 12 - Programa que ver nome e valor do produto, respondendo alguns quesitos:

soma_produto = 0
quant_produtos = 0
min_produto = 0
produto_barato = ''
total_produto = 0
while True:
    nome_produto = input('Diga o nome do produto: ')
    valor_produto = int(input('Qual o valor do produto? '))
    total_produto += 1
#A) Qual o valor total que gastou?
    soma_produto += valor_produto
#B) Quantos produtos que tem o valor maior de 1000?
    if valor_produto > 1000:
        quant_produtos += 1
#C) Qual o nome do produto mais barato?
    if total_produto == 1 or valor_produto < min_produto:
        min_produto = valor_produto
        produto_barato = nome_produto
    usuario = input('Queres continuar? [s/n] ').lower()
    if usuario == 'n':
        break
print(f' O Valor Total da compra: {soma_produto}')
print(f'A quantidade de produtos que custa mais de 1000 reais é {quant_produtos}')
print(f'O nome do produto mais barato é {produto_barato} e seu preço é {min_produto}')
'''
'''
#Exercício 13 - Fazendo um banco dando troco de R$50, 20, 10, 1.
#Minha versão da questão

valor_1 = valor_10 = valor_20 = valor_50 = 0
valor = 0
while True:
    valor_pedido = int(input('Qual o valor a ser sacado? '))
    valor = valor_pedido
    if valor % 50 == 0:
        valor_50 = valor / 50
        print(f'Total de cédulas a serem pegas é {valor_50} de R$50', end=' ')
        break
    elif valor % 20 == 0:
        valor_20 = valor / 20
        print(f'Total de cédulas a serem pegas é {valor_20} de R$20', end=' ')
        break
    elif valor % 10 == 0:
        valor_10 = valor / 10
        print(f'Total de cédulas a serem pegas é {valor_10} de R$10', end=' ')
        break
    else:
        valor_1 = valor
        print(f'Total de cédulas a serem pegas é {valor_1} de R$1', end=' ')
        break
'''
'''
#Mesma questão anterior (Versão Guanabara) -_-

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Volte sempre ao BANCO! Tenha um bom dia!')
'''
'''
#Exercício 14 - Fazendo uma tupla que o número digitado pela usuário apareça por extenso

tuplas = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente Novamente', end=' || ')
    else:
        for i in range(0, len(tuplas)):
            if num == i:
                print(f'Você digitou o número {tuplas[i]}')
        break
'''
'''
#Exercício 15 - Tupla de times, que imprima uma tupla em ordem alfabética, 
# encontre uma palavra e sua posição, quais são os 5 primeiros e os 4 ultimos colocados. 

times = (' ', "Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo","Bragantino",
         "Fluminense", "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", 
         "Chapecoense", "Corinthians", "Cruzeiro", "Vasco", "Bahia", "Vitória", 
         "Juventude", "Criciúma", "Atlético-GO")
CBF = sorted(times)
enc = times.index('Chapecoense')
print('Os 5 primeiros colocados são: ')
for i in range(1, len(times)):
    if i <= 5:
        print(f'{i}º: {times[i]}  ', end= '\n')
print('\nOs 4 ultimos colocados são: ')
for i in range(17, len(times)):
        print(f'{i}º: {times[i]}  ', end= '\n')
print(f'\n{CBF}')
print(f'\nA palavra [Chapecoense] está em posição ({enc}) na tupla')
'''
'''
#Exercício 16 - Programa que escolhe 5 números aleatórios e coloca numa tupla
#dizendo qual o maior e menor número.

num = rd.sample(range(1, 1000), k=5)
tupla = (num)
min_tup = min(tupla)
max_tup = max(tupla)
print(f'Os números escolhidos foram: {tupla}; \nO maior número é: {max_tup}; \nO menor número é: {min_tup}.')
'''
'''
#Exercício 17 - Programa que o usuário digita 4 números diferentes e coloca numa tupla, mostrando,
#quantos [9] aparece, em qual posição aparece o [3] na primeira vez e quais os números são pares

num = [int(input('Digite um número:')) for _ in range(4)]
tup = (num)
quanto_nove = tup.count(9)
num_pares = ()
pos_tres = tup.index(3) if 3 in tup else 'não encontrado'
print(tup)
for i in range(0, len(tup)):
    if tup[i] % 2 == 0:
        num_pares += (tup[i],)
    else:
        num_pares += ()
print('Esse são números pares: ')
print(num_pares)
print(f'O número [9] aparece {quanto_nove}')
print(f'O número 3 aparece na posição {pos_tres}')
'''
'''
#Exercício 18 - Nome e valor do produto colocado numa tupla, e organizando
#em tabelas de Nome e Preço do produto

nome_produto = [input('Digite o nome do produto: ') for _ in range(5)]
preço_produto = [float(input('Digite o preço do produto: R$')) for _ in range(5)]
tupla = (nome_produto, preço_produto)
print('Produtos e seus preços: ')
for i in range(0, len(tupla[0])):
    print(f'{tupla[0][i]}: R${tupla[1][i]:.2f}')
'''
'''
#Exercício 19 - Programa que ler a Tupla de palavras aleatórias, mostrando 
#a palavra e suas vogais encontradas.

palavras_variadas = (' ', "Horizonte", "Café", "Aventura", "Sussurro", "Girassol", 
                     "Janela", "Coragem", "Oceano", "Pijama", "Nostalgia", "Relâmpago", 
                     "Silêncio", "Chocolate", "Universo", "Gratidão", "Biblioteca",
                     "Neblina", "Passaporte","Eco", "Sinfonia", "Farol", "Alquimia",
                     "Orvalho", "Quimera", "Tornado", "Compasso", "Utopia", "Oásis", "Labirinto", "Eclipse")
vogais = "aeiouáéíóúâêîôûãõ"
for i in palavras_variadas[1::]:
   vogais_palavra = []
   for letra in i:
        if letra.lower() in vogais:
            vogais_palavra.append(letra)
   print(f"A palavra '{i}' tem as vogais: {vogais_palavra}")
'''