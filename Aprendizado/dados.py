def leiaDinheiro(msg):
    while True:
        preco = input(msg).replace(',','.').strip()
        if preco.isspace() or preco == '' or preco.isalpha():
            print(f'\033[1;31;40m ERRO: O {preco} é um preço inválido! \033[m')
        else:
            return float(preco)