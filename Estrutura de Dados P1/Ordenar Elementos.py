# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

print(f'\n\t Universidade de Vassouras - Maricá')
print(f'\t Estrutura de Dados - Márcio Garrido')
print(f'\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\t Avaliação da P1')

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
# Código disponibilizado pelo professor

import time
import matplotlib.pyplot as plt

def fib(elementos):
    if elementos <= 1:
        return elementos
    return fib(elementos - 1) + fib(elementos - 2)

ns = []
tempos = []

for elementos in range(0,20):
    start = time.perf_counter()
    result= fib(elementos)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(elementos)
    tempos.append(ms)

plt.plot(ns, tempos)
plt.xlabel('Valor de N')
plt.ylabel('Tempo de Execução (Micro Segundos)')
plt.show()
