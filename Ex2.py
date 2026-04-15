'''
Escreva um programa que leia um número inteiro (variável CODIGO). Verificar se o código é igual a 1, igual a 2 ou igual a 3.Caso não seja, apresentar a mensagem 
“Código inválido”. Ao ser verificado o código e constatado que é um valor válido, o programa deve verificar cada código em separado para determinar seu valor por 
extenso, ou seja, apresentar a mensagem “um”, ”dois” ou “três”. O programa deve repetir até que o usuario digite o valor -1.
'''
while True:
    codigo = int(input('Insira o código: '))
    if codigo == -1:
        print('programa parado')
        break
    elif codigo == 1:
        print('um')
    elif codigo == 2:
        print('dois')
    elif codigo == 3:
        print('três')
    else:
        print('Código Inválido')