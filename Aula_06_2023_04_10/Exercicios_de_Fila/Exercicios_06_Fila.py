# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 06) Substituir o elemento de menor valor (seja numerico ou caractere) por outro
# valor maior e apresente o resultado.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t06) Substituir o elemento de menor valor (seja numérico ou caractere) por outro \n\tvalor maior e apresente o resultado.')

import random

class Fila:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

fila = Fila()

for i in range(10):
    numero = random.randint(1, 100)
    fila.enqueue(numero)

print(f'\n\tFila Inicial:\n\t{fila.items}')

valor_minimo = min(fila.items)

indice_minimo = fila.items.index(valor_minimo)

novo_valor = valor_minimo + 1
fila.items[indice_minimo] = novo_valor

print(f'\n\tValor Minimo: {valor_minimo} Valor Substituto: {novo_valor}')

print(f'\n\tFila Final:\n\t{fila.items}')
