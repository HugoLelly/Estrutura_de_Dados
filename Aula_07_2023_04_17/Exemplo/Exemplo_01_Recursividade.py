#Exemplo de Recursividade
print(f'\n\tUniversidade de Vassouras - Maricá \n\tEstrutura de Dados - Márcio Garrido \n\t202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\tExemplo 01 Recursividade.')


def power2(n):
    if n <= 0:
        return 1
    else:
        return 2 * power2(n-1)

print(f'\n\tO resultado é: {power2 (5)}\n')
