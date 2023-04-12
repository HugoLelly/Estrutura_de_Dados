import time
import matplotlib.pyplot as plt

# Função da sequência de Fibonacci recursiva
def fib(elementos):
    if elementos <= 1:
        return elementos
    return fib(elementos - 1) + fib(elementos - 2)

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
print(f'\nresult')
# cria o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()
