def leiaINT(msg):
    while True:
        try:
             n = str(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31;40mERRO! O usuário não quis informar os dados\033[m')
            n = 0
            return int(n)
        else: 
            return int(n)
def leiaFloat(msg):
    while True:
        try:
             r = str(input(msg)).replace(',','.')
        except KeyboardInterrupt:
            print('\033[1;31;40mERRO! O usuário não quis informar os dados\033[m')
            r = 0
            return int(r)
        else: 
            return float(r)
def leiaint(msg):
    while True:
            try:
                opc = input(msg)
            except (TypeError, ValueError):
                print('\033[1;31;40mERRO! Digite uma opção correta\033[m')
            else:
                return int(opc)