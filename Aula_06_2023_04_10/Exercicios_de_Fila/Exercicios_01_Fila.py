# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 01) Escreva um programa que cria uma fila vazia e insere os números de 1 a 5
# nessa fila. Em seguida, remova os dois primeiros números da fila e exiba o
# conteúdo restante.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t01) Escreva um programa que cria uma fila vazia e insere os números de 1 a 5\n\tnessa fila. Em seguida, remova os dois primeiros números da fila e exiba o \n\tconteúdo restante.')

from Class import Fila

fila = Fila()

for i in range(1, 6):
    fila.enqueue(i)

print(f'\n\tFila Inicial:\n\t{fila.items}')

fila.dequeue()
fila.dequeue()

print(f'\n\tFila Final:\n\t{fila.items}')
