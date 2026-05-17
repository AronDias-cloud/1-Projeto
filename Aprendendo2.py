import math
import random as rd

'''
# Exercício 1 - Crie um programa que leia o nome completo de uma pessoa e mostre:

# A) O nome com todas as letras maiúsculas e minúsculas;
nome = input('Digite seu nome completo: ')
print(f"""Prefere com todas letras maiusculas {nome.upper()}!
Prefere com todas letras minusculas {nome.lower()}!""")

# B) Quantas letras ao todo (sem considerar espaços);
print(f"""Você tem {len(nome) - nome.count(' ')} letras no seu nome completo!""")

# C) Quantas letras tem o primeiro nome;
print(f"""Seu primeiro nome é {nome.split()[0] }
e ele tem {len(nome.split()[0])} letras!""")

# D) Qual é o último nome.
n = nome.split()
print(f"""Seu último nome é {n[len(n) - 1]}""")

# E) O nome contém a palavra "Silva"?
print(f"""O nome contém 'silva': {nome.lower().find('silva') >= 0}""")
'''
'''
# Exercício 2 - Crie um programa que leia um número de 0 a 9999 
# e mostre na tela cada dezena, centena e milhar.

num = int(input('Digite um número: '))
print(f"""Unidade: {num // 1 % 10}
Dezena: {num // 10 % 10}
Centena: {num // 100 % 10}
Milhar: {num // 1000 % 10}""", end='\n\n')

num2 = rd.randint(0, 9999)
print(f"""Unidade: {num2 // 1 % 10}
Dezena: {num2 // 10 % 10}
Centena: {num2 // 100 % 10}
Milhar: {num2 // 1000 % 10}""")
'''
'''
# Exercício 3 - Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com a palavra "Santo".
nome_cidade = input('Digite o nome de uma cidade: ').strip()
print(nome_cidade.lower().find('santo') >= 0)
'''
'''
# Exercício 4 - Crie um programa que leia uma frase e diga quantas 
# vezes aparece a letra "A", em que posição ela aparece pela primeira e última vez.
frase = input('Digite uma frase: ').strip()
print(frase.count('A') + frase.count('a'))
print(frase.lower().find('a'))
print(frase.lower().rfind('a'))
'''
'''
# Exercício 5 - Crie um programa que leia um número entre 0 e 10 e peça 
# para o usuário tentar adivinhar qual foi o número escolhido pelo computador.
numero_PC = rd.randint(0, 11)
numero_usuario = int(input('Digite um número entre 0 e 10: '))
if numero_usuario == numero_PC:
    print('Parabéns, você acertou!')
elif numero_usuario < numero_PC:
    print('O número é maior do que o que você digitou!')
else:    
    print('O número é menor do que o que você digitou!')
'''
'''
# Exercício 6 - Crie um programa que leia a velocidade de um carro 
# e diga se ele foi multado ou não.
velocidade_carro = float(input('Digite a velocidade do carro: '))
multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
    print(f'Você foi multado! O valor da multa é R${multa:.2f}')
else:
    print('Parabéns, você está dentro do limite de velocidade!')
'''
'''
# Exercício 7 - Crie um programa que leia a distância de uma viagem em km 
# e calcule o preço da passagem. 
distancia_km = float(input('Digite a distância da viagem em km: '))

# cobrando R$0,50 por km para viagens de até 200 km 
if distancia_km <= 200:
    valor_passagem = distancia_km * 0.50
else: 
# e R$0,45 por km para viagens mais longas.
    valor_passagem = distancia_km * 0.45
print(f'O valor da passagem é R${valor_passagem:.2f}')
'''
'''
# Exercício 8 - Crie um programa que leia um ano e diga se ele é bissexto ou não.
ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[7;32;44m{ano} é um ano bissexto!\033[m')
else:
    print(f'\033[4;30;41m{ano} não é um ano bissexto!\033[m')
'''
'''
# Exercício 9 - Crie um programa que leia três números 
# e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f'O maior número é {maior} e o menor número é {menor}.')
'''
'''
# Exercício 10 - Crie um programa que leia o salário de um funcionário
# e mostre o valor do aumento. 
salario = float(input('Digite o salário do funcionário: R$'))
if salario <= 1250:
# Para salários inferiores a R$1250,00, calcule um aumento de 15%.
    aumento = salario * 0.15
    print(f"""O salário do funcionário
com o aumento de 15% é R${salario + aumento:.2f}""")
else:
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
    aumento = salario * 0.10
    print(f"""O salário do funcionário
com o aumento de 10% é R${salario + aumento:.2f}""")
'''
'''
# Exercício 11 - Crie um programa que leia o comprimento de três retas
# e diga se elas podem ou não formar um triângulo.
retas = [float(input('Digite o comprimento de uma reta: '))
          for _ in range(3)]
soma_lados = sum(retas)
maior_reta = max(retas)
if soma_lados - maior_reta > maior_reta:
    print('\033[1;32;44mAs retas formam um triângulo!\033[m')
else:
    print('\033[1;34;42mAs retas não formam um triângulo!\033[m')
'''

# Exercício 12 - Um "Hello, World!" que quando imprimido, 
# o terminal fica com formatação diferente.
print('\033[1;32;44mOlá, Mundo!\033[m')
