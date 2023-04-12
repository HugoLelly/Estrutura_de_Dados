# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 02) Escreva um programa que cria uma fila vazia e insere 10 numeros aleatorios
# nessa fila, em seguida, remova todos os numeros pares da fila e exiba o conteudo
# restante.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t02) Escreva um programa que cria uma fila vazia e insere 10 números aleatórios \n\tnessa fila, em seguida, remova todos os números pares da fila e exiba o conteúdo \n\trestante.')

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

fila_filtrada = Fila()

while not fila.is_empty():
    numero = fila.dequeue()
    if numero % 2 != 0:
        fila_filtrada.enqueue(numero)

print(f'\n\tFila Final:\n\t{fila_filtrada.items}')
