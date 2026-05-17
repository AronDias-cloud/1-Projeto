import math
import random as rd
import emoji
import time

# Exercício 1 - Faz uma prestação salarial com base no valor da casa e de suas parcelas anuais

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite a quantidade de anos para pagar: "))
prestacao = valor_casa / (anos * 12)
if prestacao > (salario * 0.3):
    print(emoji.emojize("Empréstimo negado! :thumbs_down:"))
elif prestacao == (salario * 0.3):
    print(emoji.emojize("Empréstimo aprovado, mas cuidado! :warning:"))
else:
    print(emoji.emojize("Empréstimo aprovado! :thumbs_up:"))


# Exercício 2 - Escolha uma opção (Binário, Octadecimal, Hexadecimal)
#e coloca um número(s) que seja criptografado pela opção escolhida

num = int(input("Digite um número de 1 a 3: "))
if num == 1:
    num2 = int(input("Digite algum número aqui: "))
    binario = bin(num2)
    print(f"O número {num2} em binário é: {binario}")
elif num == 2:
    num2 = int(input("Digite algum número aqui: "))
    octal = oct(num2)
    print(f"O número {num2} em octal é: {octal}")
elif num == 3:
    num2 = int(input("Digite algum número aqui: "))
    hexadecimal = hex(num2)
    print(f"O número {num2} em hexadecimal é: {hexadecimal}")

# Exercício 3 - Mostra qual o número é maior, menor e igual

num = int(input("Digite um número inteiro: "))
num1 = int(input("Digite outro número inteiro: "))
if num > num1:
    print(f"O número {num} é maior que o número {num1}.")
elif num < num1:
    print(f"O número {num} é menor que o número {num1}.")
else:
    print(f"Os números {num} e {num1} são iguais.")
'''
'''
# Exercício 4 - Se a pessoa tem a idade adequada para se alistar ou não
#e quanto falta ou se passou da data de alistar
data_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - data_nascimento

if idade < 18:
    print(f"Você tem {idade} anos, ainda vai se alistar.")
    quanto_tempo_falta = 18 - idade
    print(f"Falta {quanto_tempo_falta} anos para você se alistar.")
elif idade > 17 and idade < 19:
    print(f"Você tem {idade} anos, está na hora de se alistar.")
else:
    print(f"Você tem {idade} anos, já passou do tempo de se alistar.")
    já_passou = idade - 19
    print(f"Já passou {já_passou} anos do tempo de se alistar.")

# Exercício 4 - Mostra qual categoria a pessoa está, com base na idade da pessoa.

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(f"Você tem {idade} anos, categoria MIRIM.")
elif idade <= 14:
    print(f"Você tem {idade} anos, categoria INFANTIL.")
elif idade <= 19:
    print(f"Você tem {idade} anos, categoria JUVENIL.")
elif idade <= 20:
    print(f"Você tem {idade} anos, categoria ADULTO.")
else:
    print(f"Você tem {idade} anos, categoria MASTER.")

# Exercício 5 - Pega 3 retas e diga se elas são Equilátero, Isósceles ou Escaleno
retas = [int(input(f'Qual o tamanho da [i+1] reta')) for i in range(3)]
if retas[0] == retas[1] == retas[2]:
    print("As retas formam um triângulo equilátero.")
elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
    print("As retas formam um triângulo isósceles.")
else:
    print("As retas formam um triângulo escaleno.")

# Exercício 6 - Faz o calculo do IMC da pessoa e diz sua categoria 

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print(f"Seu IMC é {imc:.2f}, você está com o peso ideal.")
elif imc > 25 and imc < 30:
    print(f"Seu IMC é {imc:.2f}, você está com sobrepeso.")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade.")
else:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade mórbida.")

# Exercício 7 - Como vai ser pago o produto, a vista ou no cartão?
#Dependendo da opção, vai ter desconto ou juros no produto

dinheiro = float(input("Digite o valor do produto: R$"))
num = int(input("Digite um número entre 1 e 2: "))
if num == 1:
    cheque = 0.1
    a_vista = dinheiro - (dinheiro * cheque)
    print(f"Valor a ser pago à vista no papel: R${a_vista:.2f}")
elif num == 2:
    cartao = int(input("Vai ser dividido em quantas vezes? "))
    if cartao == 1:
      cartao = 0.05
      a_vista = dinheiro - (dinheiro * cartao)
      print(f"Valor a ser pago à vista no cartão: R${a_vista:.2f}")
    elif cartao == 2:
      print(f"Valor a ser pago em 2 vezes no cartão: R${dinheiro:.2f}")
    elif cartao == 3:
      cartao = 0.2
      valor_parcela = dinheiro + (dinheiro * cartao)
      print(f"Valor a ser pago em 3 vezes no cartão: R${valor_parcela:.2f}")

# Exercício 8 - Jogo de Pedra, Papel e Tesoura

jogo = rd.choice(["pedra", "papel", "tesoura"])
jogo1 = input("Digite pedra, papel ou tesoura: ").lower()
if jogo1 == jogo:
    print("Empate!")
elif (jogo1 == "pedra" and jogo == "tesoura") or (jogo1 == "papel" and jogo == "pedra") or (jogo1 == "tesoura" and jogo == "papel"):    
    print("Você ganhou!")
else:  
    print("Você perdeu!")

# Exercício 9 - Contagem regressiva para final de ano, usando emojis.

num = int(input("Digite uma contagem regressiva em segundos: "))
for i in range(num, 0, -1):
    print(i)
    pausa = 1  
    time.sleep(pausa)
print(emoji.emojize("Feliz ano novo! :collision::vulcan_salute:"))

# Exercício 10 - Números que sejam impar e multiplos de 3 somados dão?

total = 0
for i in range(1, 500 + 1):
 if i % 2 == 0:
     print(' ')
 elif i % 3 == 0:
        total = total + i
        print(f'Os números {i} impares e multiplo de 3 somados dão {total}.')

# Exercício 11 - Digite 7 números que são pares ou impares e some os pares

num = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(7)]
total = 0
for n in num:
    if n % 2 == 0:
        total += n
        print(f"Os números {n} são pares.")
    else:
        print(f"Os números {n} são ímpares.")    
print(f"A soma dos números pares é {total}.")

# Exercício 12 - Progressão Aritmetica (Parte 1)

primeiro = int(input(f"Digite o primeiro termo: "))
r = int(input(f"Digite a razão da progressão: "))
decimo = primeiro + (10 - 1) * r
for i in range(primeiro, decimo + r, r):
    print(f'{i}', end=' -> ')
print('FIM')

# Exercício 13 - Progressão Aritmetica (Parte 2) 

a = [int(input(f"Digite o {i+1}º termo: ")) for i in range(12)]
razao = a[1] - a[0]
for n in range(1, len(a) - 1):
    if a[n + 1] - a[n] != razao:
        print("A sequência não é uma progressão aritmética.")
        break
else:
    for num in range(len(a)):
       s = (a[0] + a[num]) * num / 2
    print(f"A razão da progressão é {razao}.")
    print("Os 10 primerios termos da progressão são:")
    for i in range(10):
        print(a[i])
    print(f"A soma de todos os Termos é {s}.")

# Exercício 14 - Veja se o número é primo ou divisivel por 3 ou 2

num = int(input("Digite um número inteiro: "))
for i in range(num, num + 1):
    if i % 2 != 0:
        if i % 3 != 0:
            print(f"O número {i} é primo.")
        else:
            print(f"O número {i} é divisivel por 3.")
    else:
        print(f"O número {i} é divisivel por 2.")

# Exercício 14 - Veja se a frase é um palíndromo

text = input("Digite uma frase: ").replace(" ", "").lower()
if text == text[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")

# Exercício 15 - Veja as informações de 4 pessoas (Nome, idade e sexo), e diga 
#media das idades, quem é o homem mais velho e quantas mulheres com menos de 20 anos

soma_idade = 0
idade_max = 0
nome_mais_velho = ''
total_mulher = 0
for i in range(1, 5):
    print(f'----- {i} PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').lower().strip()
    soma_idade += idade
    if sexo == 'm' and idade > idade_max:
       idade_max = idade
       nome_mais_velho = nome
    if sexo == 'f' and idade < 20:
       total_mulher += 1
media_idade = soma_idade / 4
print(f'A média das idades é {media_idade}')
if nome_mais_velho != '':
        print(f'O homem mais velho é {nome_mais_velho} com a idade {idade_max}')
print(f'A quantidade de mulheres menor de 20 anos é: {total_mulher}')
