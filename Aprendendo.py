import math
import random as rd
import emoji
import moviepy as mpy
import pygame as pg
'''
# Exercício 1: Analisando os tipos primitivos
a = (input('Digite alguma coisa: '))
print('O tipo primitivo desse valor é', type(a))
print('Tem maiusculo?' , a.isupper())
print('Tem minusculo?' , a.islower())
print('Tem espaço?' , a.isspace())
print('Tem um numéro?' , a.isnumeric())
print('Tem alfabeto?' , a.isalpha())
print('Tem alfanumérico?' , a.isalnum())
print('Está capitalizada?' , a.istitle())
print('Tem acento? ' , a.isascii())
'''
'''
# Exercício 2: Operadores Aritméticos
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
s = num + num1
s1 = num - num1
s2 = num * num1
s3 = num / num1
s4 = num // num1
s5 = num ** num1
s6 = num % num1
print(f'A soma é {s}', end=' >>> ')
print('A subtração é', s1, end=' >>> ')
print('A multiplicação é', s2, end=' >>> ')
print(f'A divisão é {s3:.3f}', end=' >>> ')
print('A divisão inteira é', s4, end=' >>> ')
print('A potência é', s5, end=' >>> ')
print('O módulo é', s6,)
'''
'''
# Exercício 3: Antecessor e Sucessor; Dobro, Triplo e Raiz Quadrada
n = int(input('Digite um número: '))
print('O número {} é antecessor de {} e sucessor de {}'.
      format(n, n+1, n-1))
print(f'O dobro de {n} é {n*2} \n O triplo é {n*3} e a raiz quadrada de {n} é {n**0.5:.2f}')
'''
'''
# Exercício 4: Conversor de Moedas
real = float(input('Diga quanto você tem na carteira: '))
dolar = real / 4.99
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
'''
'''
# Exercício 5: Calculando a área de uma parede
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'A área da parede é {area}m² e você precisará de {tinta}L de tinta para pintá-la.')
'''
'''
# Exercício 6: Calculando o desconto do produto e o aumento salarial
preço = float(input('Digite o preço do produto: R$'))
desconto = preço * 0.05
preço_final = preço - desconto
print(f'De R${preço:.2f} do produto', end=' ') 
print(f'com 5% de desconto, você pagará R${preço_final:.2f}.   ')

salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 0.15
salario_final = salario + aumento
print(f'O salário do funcionário é R${salario:.2f}', end=' e ') 
print(f'com o aumento de 15%, ele passará a receber R${salario_final:.2f}.')
'''
'''
# Exercício 7: Conversor de Medidas
numero = int(input('Digite uma medida: '))
km = numero / 1000
hm = numero / 100
dam = numero / 10
dm = numero * 10
cm = numero * 100
mm = numero * 1000
print(f'A medida de {numero}m é equivalente a \n {dam}dam \n {hm}hm \n {km}km \n {dm}dm \n {cm}cm \n {mm}mm.')
'''
'''
# Exercício 8: Gerando um número aleatório e calculando a raiz quadrada
num = rd.randint(1, 100)
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é \n de forma arredondada pra acima é ({math.ceil(raiz)}) \n e sem arrendodandamento ({raiz:.2f}).')
'''
'''
# Exercício 9: Colocando emojis no código
print(emoji.emojize('Olá, mundo! :globe_showing_Americas:'))
print(emoji.emojize('Você é muito legal :homem::polegar_para_cima:', language='pt'))
'''
'''
# Exercício 10: Usando a biblioteca math para arredondar um número e calcular a hipotenusa
num = float(input('Digite um número não inteiro: '))
print(f'O número {num} tem a parte inteira {math.ceil(num)}.')
'''
'''
# Exercício 11: Calculando a hipotenusa de um triângulo retângulo usando a função hypot da biblioteca math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa do triângulo retângulo com catetos {cateto_oposto} e {cateto_adjacente} é {hipotenusa:.2f}.')
'''
'''
# Exercício 12: Calculando o seno, cosseno e tangente de um ângulo usando a biblioteca math
angulo_graus = float(input('Digite um ângulo em graus: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f"""O seno do ângulo é {seno:.2f}; 
      \n O cosseno é {cosseno:.2f}; 
      \n A tangente é {tangente:.2f}.""")
'''
'''
# Exercício 13: Escolhendo um aluno para apresentar um trabalho usando a biblioteca random
nome = ['Aron', 'Bruno', 'Carlos', 'Daniel', 'Eduardo']
nome2 = rd.choice(nome)
print(f'O Professor escolheu... {nome2}.')
nome3 = rd.sample(nome, 5)
print(f'O primeiro a apresentar é... {nome3[0]}.')
print(f'O segundo a apresentar é... {nome3[1]}.')
print(f'O terceiro a apresentar é... {nome3[2]}.')
print(f'O quarto a apresentar é... {nome3[3]}.')
print(f'O quinto a apresentar é... {nome3[4]}.')
'''
'''
# Exercício 14: Criando um vídeo simples usando a biblioteca moviepy
pg.init()
pg.mixer.music.load('Night_2_-No_Im_Not_a_Human.ogg')
pg.mixer.music.play()
#pg.time.delay(10000)
input()
pg.event.wait()
'''
# Exercício 15: Manipulando strings
frase = 'Curso em Vídeo Python'
print(frase[:19:2])
print(frase.count('o', 0, 15))
print(frase.find('deo'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.split())
print('-'.join(frase))
print("""Estou aprendendo Python!
para depois criar projetos reais 
e seguir para analise de dados""")