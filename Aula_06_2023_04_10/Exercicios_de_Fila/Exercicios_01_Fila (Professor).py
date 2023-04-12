# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 01) Escreva um programa que cria uma fila vazia e insere os números de 1 a 5
# nessa fila. Em seguida, remova os dois primeiros números da fila e exiba o
# conteúdo restante.

class Fila:
    def _init_(self):
        self.items = []

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Criando a fila e adicionando os valores
valores_numericos = Fila()
valores_numericos.enqueue(1)
valores_numericos.enqueue(2)
valores_numericos.enqueue(3)
valores_numericos.enqueue(4)
valores_numericos.enqueue(5)

# Método manual - Removendo os dois primeiros valores da fila
#valores_numericos.dequeue()
#valores_numericos.dequeue()

# Mátodo automático - Removendo uma quantidade variável de valores da fila
quantidade = 2
for i in range(quantidade):
    valores_numericos.dequeue()


# Exibindo o conteúdo restante
while not valores_numericos.is_empty():
    fila_atual = valores_numericos.dequeue()
    print(f"Fila atual: {fila_atual}")
