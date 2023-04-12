# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

import time
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def ordenar(elementos):
    elementos_ordenada = elementos.copy()
    elementos_ordenada = sorted([elem for sublist in elementos for elem in sublist])
    if imprimiu:
        print(f'\n\t Elementos em Ordem Crescente: \n\t', elementos_ordenada)
    elementos_ordenada = sorted([elem for sublist in elementos for elem in sublist], reverse=True)
    if imprimiu:
        print(f'\n\t Elementos em Ordem Decrescente: \n\t', elementos_ordenada)

def executar():
    global imprimiu
    imprimiu = True
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

        imprimiu = False

    plt.scatter(ns, tempos)
    plt.yscale('log')
    plt.xlabel('Tamanho dos Elementos (n)')
    plt.ylabel('Tempo de Execução (Microssegundos)')
    plt.title('Tempo de Execução vs Tamanho dos Elementos (Big O)')
    plt.plot(ns, [n * n * (1.0/3.0) for n in ns], 'r', label='O(n*log n)')
    plt.legend()

    # Cria um novo frame com o gráfico
    fig_canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_frame)
    fig_canvas.get_tk_widget().grid(row=0, column=0)
    fig_canvas.draw()


# Matriz de elementos
elementos = [[0, 1, 2, 3],
             [11, 12, 13, 4],
             [10, 15, 14, 5],
             [9, 8, 7, 6]]

imprimiu = True

root = tk.Tk()
root.title("Gráfico")
root.geometry("800x600")

# Cria um frame para o gráfico
graph_frame = tk.Frame(root)
graph_frame.pack(fill=tk.BOTH, expand=True)

# Cria um botão para executar o código e exibir o gráfico
button = tk.Button(root, text="Executar", command=executar)
button.pack(pady=10)

root.mainloop()
