# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t Avaliação da P1')

import time
import matplotlib.pyplot as plt

def ordenar(elementos): #Função para ordenar os elementos

  elementos_ordenada = elementos.copy() #Cria uma cópia dos elementos

  elementos_ordenada.sort() #Ordena os elementos de forma crescente

  print(f'\n\t Elementos em Ordem Cresente: \n\t', elementos_ordenada) #Exibe os elementos de forma cresente

  elementos_ordenada.sort(reverse=True) #Inverte os elementos em ordenando em forma decrescente

  print(f'\n\t Elementos em Ordem Decresente: \n\t', elementos_ordenada) #Exibe os elementos de forma decrescente

#Elementos para ordenar
a = [0,1,2,3]
b = [11,12,13,4]
c = [10,15,14,5]
d = [9,8,7,6]
elementos = a + b + c + d

print(f'\n\t Elementos para Ordenar: \n\t', a , b , c , d) #Exibe os elementos

ordenar(elementos) #Função de ordenar os elementos

# Notação Big O:
# O(n log n)

# Função da sequência de Fibonacci recursiva

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# listas para armazenar os valores de n e o tempo de execução
ns = []
tempos = []

# testa a função para vários valores de n
for n in range(1, 31):
    start = time.perf_counter()
    result= fib(n)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(n)
    tempos.append(ms)
print(result)

# cria o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()
