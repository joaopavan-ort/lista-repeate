# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

x, y = map(int, input('Insira dois nº inteiros: ').split())
if x <= y:
    for i in range(x, y+1):
        print(i, end='  ')
else:
    for i in range(x, y-1, -1):
        print(i, end='  ')