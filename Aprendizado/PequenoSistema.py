import os
import json
import time

ARQUIVO_DADOS = 'dados_cadastrados.json'
c = ('\033[m', '\033[1;37m', '\033[0;37m', '\033[1;34m', '\033[1;31m', '\033[0;33m' )

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except:
            return []  
    return []

def salvar_dados(lista_de_pessoas):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_pessoas, arquivo, indent=4, ensure_ascii=False)
        
def titulo(msg, cor=0):
    print('='*40)
    print(c[cor], end='')
    print(f'{msg}'.center(40))
    print(c[0], end='')
    print('=' *40)
    time.sleep(0.2)
    
def opção1(msg, cor=0):
    print(c[cor], end="")
    print(f'{msg} -', end='')
    print(c[0], end="")
    
def opção(msg, cor=0):
    print(c[cor], end="")
    print(f' {msg} ')
    print(c[0], end="")
    time.sleep(0.2)
    
def cadastro():
    inf = {}
    while True:
        try:
            nome = str(input('Nome: '))
            if nome == '' or not nome.replace(' ', '').isalpha():
                print('\033[1;31;40mERRO! Digite um nome válido.\033[m')
            else:
                inf['Nome'] = nome
                break
        except KeyboardInterrupt:
            print('\n\033[1;31;40mERRO! O usuário não quis informar o nome.\033[m')
            return None
    while True:
        try:    
            idade = input('Idade: ').strip()
            if not idade.isdigit():
                print('\033[1;31;40mERRO! Digite uma idade válida (número inteiro).\033[m')
            else:
                inf['Idade'] = int(idade)
                break
        except KeyboardInterrupt:
            print('\n\033[1;31;40mERRO! O usuário não quis informar a idade.\033[m')
            return None
    print(f"Novo registro de {inf['Nome']} adicionado.")
    return inf

def lista(dados):
    dados_validos = [p for p in dados if p and 'Nome' in p and 'Idade' in p]
    if len(dados_validos) == 0:
        print("Nenhuma pessoa cadastrada ainda.")
    else:
        for pessoa in dados:
            try:
                print(f"{pessoa['Nome']:<24}{pessoa['Idade']:>11} anos")
            except KeyError:
                print(f'\033[1;31;40mERRO! O valor (idade) é desconhecido \033[m')
banco_dados = carregar_dados()
