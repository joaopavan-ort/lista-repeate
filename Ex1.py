# Escreva um programa que imprima na tela a soma dos números ímpares entre 1 e 30 e a multiplicação dos números pares entre 1 e 30.
soma = 0
for x in range(1, 30, 2):
    soma += x
    print(x, soma)
print('Soma:', soma)

print()

mult = 1
for x in range(2, 31, 2):
    mult *= x
    print(x, mult)
print('Multiplicação:', mult)