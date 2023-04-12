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

    def inverter(self):
            pilha = []
            while not self.is_empty():
                pilha.append(self.dequeue())

            while pilha:
                self.enqueue(pilha.pop())
