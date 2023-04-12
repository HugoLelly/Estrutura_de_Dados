# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

print(f'\n\t Universidade de Vassouras - Maricá')
print(f'\t Estrutura de Dados - Márcio Garrido')
print(f'\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\t Avaliação da P1')

import time
import matplotlib.pyplot as plt

def ordenar(elementos):
    elementos_ordenada = elementos.copy()
    elementos_ordenada = sorted([elem for sublist in elementos for elem in sublist])
    if imprimiu:
        print(f'\n\t Elementos em Ordem Crescente: \n\t', elementos_ordenada)
    elementos_ordenada = sorted([elem for sublist in elementos for elem in sublist], reverse=True)
    if imprimiu:
        print(f'\n\t Elementos em Ordem Decrescente: \n\t', elementos_ordenada)

# Matriz de elementos
elementos = [[0, 1, 2, 3],
             [11, 12, 13, 4],
             [10, 15, 14, 5],
             [9, 8, 7, 6]]

imprimiu = True # Variável de controle para imprimir apenas na primeira iteração

print(f'\n\t Elementos para Ordenar: \n\t', elementos)

ordenar(elementos)

ns = []
tempos = []

for n in range(1, 31):
    start = time.perf_counter()
    ordenar(elementos)
    end = time.perf_counter()
    ms = (end - start) * 10**6
    ns.append(n)
    tempos.append(ms)

    imprimiu = False # Desativa a impressão a partir da segunda iteração

plt.scatter(ns, tempos)
plt.yscale('log') # Escala logarítmica no eixo y
plt.xlabel('Tamanho dos Elementos (n)')
plt.ylabel('Tempo de Execução (Microssegundos)')
plt.title('Tempo de Execução vs Tamanho dos Elementos (Big O)')
plt.plot(ns, [n * n * (1.0/3.0) for n in ns], 'r', label='O(n*log n)') # Adiciona a linha O(n*log n)
plt.legend()
plt.show()
