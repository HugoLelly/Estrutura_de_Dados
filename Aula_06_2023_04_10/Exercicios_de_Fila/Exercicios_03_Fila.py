# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 03) Escreva um programa que cria uma fila vazia e insere os numeros de 1 a 10
# nessa fila. em seguida, exiba o elemento que esta na posição 4 da fila.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t03) Escreva um programa que cria uma fila vazia e insere os números de 1 a 10 \n\tnessa fila. Em seguida, exiba o elemento que esta na posição 4 da fila.')

from Class import Fila

fila = Fila()

for i in range(1, 11):
    fila.enqueue(i)

posicao = 4
if posicao <= fila.size():
    elemento = fila.items[posicao - 1]
    print(f'\n\tFila Inicial:\n\t{fila.items}')
    print(f'\n\tO elemento na posição {posicao} da fila é: {elemento}')
else:
    print(f'\n\tA posição {posicao} está fora do tamanho da fila.')
