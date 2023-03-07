# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 06) Criar uma tupla com números inteiros e verificar se um determinado número está na tupla ou não. 

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 06) Criar uma tupla com números inteiros e verificar se um determinado número está na tupla ou não.')

tupla_numeros = (9, 4, 23, 7, 8, 92, 3, 11)

numero_verificar = int(input(f'\n\t Digite um número para verificar se está na tupla: '))

if numero_verificar in tupla_numeros:
    print(f'\n\t O número {numero_verificar} está na tupla!')
else:
    print(f'\n\t O número {numero_verificar} não está na tupla!')