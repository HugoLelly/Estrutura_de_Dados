# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 05) Remover o elemento de maior valor (seja numerico ou caractere)

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t05) Remover o elemento de maior valor (seja numérico ou caractere).')

from Class import Fila

import random

fila = Fila()

for i in range(10):
    numero = random.randint(1, 100)
    fila.enqueue(numero)

print(f'\n\tFila Inicial:\n\t{fila.items}')

valor_maximo = max(fila.items)

fila.items.remove(valor_maximo)

print(f'\n\tValor Maximo Removido {valor_maximo}')

print(f'\n\tFila Final:\n\t{fila.items}')

