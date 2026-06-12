def aumentar(preco=0, tax=0):
    """
    -> Calcula o aumento de um preço
    :param preco: O preço a ser aumentado
    :param tax: A porcentagem do aumento
    :return: O valor do aumento
    """
    return preco + (preco * tax / 100)
def diminuir(preco=0, tax=0):
    """
    -> Calcula a redução de um preço
    :param preco: O preço a ser reduzido
    :param tax: A porcentagem da redução
    :return: O valor da redução
    """
    return preco - (preco * tax / 100)
def dobro(preco=0):
    """
    -> Calcula o dobro de um preço
    :param preco: O preço a ser dobrado
    :return: O valor do dobro
    """
    return preco * 2
def metade(preco=0):
    """
    -> Calcula a metade de um preço
    :param preco: O preço a ser dividido
    :return: O valor da metade
    """
    return preco / 2
def moeda(preco=0, moeda='R$'):
    """
    -> Formata um valor como moeda
    :param preco: O preço a ser formatado
    :param moeda: O símbolo da moeda
    :return: O valor formatado como moeda
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')
def resumo(preco=0, tax_aum=1, tax_red=1):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{"Preço analisado:":<27}{moeda(preco):>11}')
    print(f'{"Dobro do preço:":<27}{moeda(dobro(preco)):>11}')
    print(f'{"Metade do preço:":<27}{moeda(metade(preco)):>11}')
    print(f'{f"{tax_aum}% de aumento:":<27}{moeda(aumentar(preco, tax_aum)):>11}')
    print(f'{f"{tax_red}% de redução:":<27}{moeda(diminuir(preco, tax_red)):>11}')
    print('-' * 40)