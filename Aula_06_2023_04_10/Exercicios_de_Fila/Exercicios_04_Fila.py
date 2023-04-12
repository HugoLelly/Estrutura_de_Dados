# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 04) Inverter a fila

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t04) Inverter a fila.')

from Class import Fila

fila = Fila()

for i in range(1, 11):
    fila.enqueue(i)

print(f'\n\tFila Inicial:\n\t{fila.items}')

fila.inverter()

print(f'\n\tFila Final:\n\t{fila.items}')
