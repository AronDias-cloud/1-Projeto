"""
# Salário do 1º Funcionário
salario_mensal = float(input("Digite o valor do salário mensal: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora1 = float(salario_mensal) / (horas_trabalhadas)

# Salário do 2º Funcionário
salario_mensal1 = (input("Digite o valor do salário mensal: "))
horas_trabalhadas1 = float(input("Digite o número de horas trabalhadas: "))
valor_hora2 = float(salario_mensal1) / (horas_trabalhadas1)

# Comparação do valores/horas entre os 2 funcionarios.
if valor_hora1 > valor_hora2:
    print("O valor da hora trabalhada 1 é maior do que o valor da hora trabalhada 2.")
else:
    print("O valor da hora trabalhada 2 é menor do que o valor da hora trabalhada 1.")

# Comparação 1º Funcionário de acordo com valor/hora ganho.
if valor_hora1 < 7.37:
    print("O valor da hora trabalhada 1 é inferior ao salário mínimo ou você é um jovem aprendiz. " + str(valor_hora1))
elif valor_hora1 >= 7.37 and valor_hora1 < 11.30:
    print("O valor da hora trabalhada 1 é igual ou acima do salário mínimo. " + str(valor_hora1))
elif  valor_hora1 >= 11.30 and valor_hora1 < 16.00:
    print("O valor da hora trabalhada 1 é acima de 2 salários mínimos. " + str(valor_hora1))
elif valor_hora1 >= 16.00 and valor_hora1 < 90.90:
    print("O valor da hora trabalhada 1 é considerado igual ou acima de um bom salário familiar no Brasil. " + str(valor_hora1))
elif valor_hora1 >= 90.90:
    print("O valor da hora trabalhada 1 é considerado rico no Brasil. " + str(valor_hora1))  
else:
    print("O valor da hora trabalhada é considerado muito rico no Brasil." + str(valor_hora1))

#Aqui foi para aprender um pouco do loop (For)
for i in range(1, 11):
   print(f"{i} x {valor_hora1} = {i * valor_hora1}")

#Aqui foi a primeira vez que usei os comandos (FOR) e (IF e ELSE)      
senha = input("Digite a senha: ")
for senhas in senha:
if len(senhas) >= 6:  
    print("Acesso permitido.")
 else:    
    print("Acesso negado.")
"""

"""
#Aqui foi quando usei o comando (.append) para add para outra variavel (Lista) vazia
salario_dos_funcionarios = []
total = 0
for i in range(5):
    salario = float(input("Digite o salário do funcionário: "))
    salario_dos_funcionarios.append(salario)
for salario in salario_dos_funcionarios:
   if salario_dos_funcionarios[i] < 4:
     total = total + salario
     print(f"Salário: {total}")
"""


"""
#Aqui foi quando usei o comando (WHILE e IF/ELSE) para criar uma código de login
usuario = ""
senha = ""
tentativas = 0
while (usuario != "Aron" or senha != "123456") and tentativas < 3:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    tentativas += 1
    if usuario == "Aron" and senha == "123456":
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
        
"""
'''
#Aqui eu criei um código que resolvesse Fatoriais
num = int(input("Digite um número inteiro: "))
total = 1
if num <= 0:
    print("O número invalido, digite um número inteiro positivo diferente de zero.")
while num > 1:
    print(f"{total} x {num} = ")
    total = total * num
    print(f"{total}")
    num -= 1

'''

'''
#Aqui foi para criar um triângulo retângular com asterisco usando WHILE e FOR
n = "*"
for i in range(1, 5):
    print(n * i)
n = "*"
while len(n) < 5:
    print(n)
    n += "*"
'''
'''
#Aqui usei FUNÇÕES para resolver essas duas somas usando FOR
def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

'''
'''
#Aqui usei funções para transformar comuns em romanos
def romano(nom):
   n = (1, 5, 10, 50, 100, 500, 1000)
   r = ("I", "V", "X", "L", "C", "D", "M")
       
   for i in range(len(n) - 1, -1, -1):
           if nom < n[1] and nom >  n[0]:
               print(r[0] + r[1], end="")
               break
           elif nom < n[2] and nom >  n[1]:
               print(r[0] + r[2], end="")
               break
           while nom >= n[i]:
               print(r[i], end="")
               nom -= n[i]
n2 = romano(2028)
'''
#Aqui foi para ser o contrário do anterior, romanos para comuns
n = [1, 5, 10, 50, 100, 500, 1000]
r = ["I", "V", "X", "L", "C", "D", "M"]
nom = ["M", "M", "X", "X", "I", "V"]
total = 0
for i in range(len(nom)):
    for j in range(len(r)):
        
        while nom[i] == r[j]:
            total += n[j]
            print(total)
            break
        
        



