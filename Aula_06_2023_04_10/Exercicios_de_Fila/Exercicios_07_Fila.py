# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 07) organizar a fila de forma crescente (prioridade por idade)

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t07) Organizar a fila de forma crescente (prioridade por idade).')

from Class import Fila

import random

fila = Fila()

for i in range(10):
    numero = random.randint(1, 100)
    fila.enqueue(numero)

print(f'\n\tFila Inicial:\n\t{fila.items}')

fila.items = sorted(fila.items)

print(f'\n\tFila Final:\n\t{fila.items}')
