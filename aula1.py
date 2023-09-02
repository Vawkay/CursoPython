"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Recebe valor do usuário
entrada = input("Digite um número inteiro: ")
# Verifica se o valor é digito numérico
if entrada.isdigit():
    # Converte o valor para inteiro
    numero = int(entrada)
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
else:
    print("O valor digitado não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Recebe o valor do usuário
entrada = input("Digite a hora atual: ")
# Verifica se o valor é digito numérico
if entrada.isdigit():
    # Converte o valor para inteiro
    hora = int(entrada)
    # Verifica se a hora está entre 0 e 11
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    # Verifica se a hora está entre 12 e 17
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    # Verifica se a hora está entre 18 e 23
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    # Se não estiver entre 0 e 23, exibe mensagem de erro
    else:
        print("Hora inválida")
else:
    print("Digite um valor inteiro para a hora")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Recebe o valor do ususário
nome = input("Digite seu primeiro nome: ")
# Verifica o tamanho do nome   
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
