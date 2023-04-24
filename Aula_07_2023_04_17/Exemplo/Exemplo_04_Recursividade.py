#Exemplo de Recursividade
print(f'\n\tUniversidade de Vassouras - Maricá \n\tEstrutura de Dados - Márcio Garrido \n\t202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\tExemplo 04 Recursividade.')


def factorial(n):
    if n <= 1:
        return 1
    else:
        return 2 * factorial(n-1)

print(f'\n\tO resultado é: {factorial (5)}\n')
