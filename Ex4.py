# Desenvolva um programa em python que leia o nome e a idade de 7 pessoas e mostre o nome da pessoa mais velha e o nome da pessoa mais nova.
nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))

jovem = nome
menor = idade

velho = nome
maior = idade

for i in range(6):
    nome = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    if idade < menor:
        jovem = nome
        menor = idade
    elif idade > maior:
        velho = nome
        maior = idade
print('Mais novo:', jovem, menor, 'anos')
print('Mais velho:', velho, maior, 'anos')