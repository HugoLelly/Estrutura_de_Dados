# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 01) Popular randomicamente a pilha e imprimir todos os números pares.

import random

print(f'\n\t 01) Popular randomicamente a pilha e imprimir todos os números pares.')

pilha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'\n\t A Pilha é: {pilha}')

random.shuffle(pilha)

print(f'\n\t A Pilha Randomica é: {pilha}')

print(f'\n\t Os numeros pares são: \n')

for numero in pilha:
    if numero % 2 == 0:
        print(f'\t {numero}')
print(f'\n')

print(f'\n\t 02) Inverter a pilha anterior.')

invertida = reversed(2)

print(f'\n\t A Pilha invertida é: {invertida}')