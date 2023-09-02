"""Calculadora simples com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
        numeros_validos = False

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao inválidos')
        continue

    operadores_permitdos = ['+', '-', '*', '/']
    if operador not in operadores_permitdos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Calculando...')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
    


    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair:
        print('Até logo')
        break