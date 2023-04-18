#Exemplo de Recursividade
print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\tExemplo 04 Recursividade.')


def factorial(n):
    if n <= 1:
        return 1
    else:
        return 2 * factorial(n-1)

print(f'\n\tO resultado é: {factorial (5)}\n')
