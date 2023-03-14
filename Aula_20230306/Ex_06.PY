# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 06) Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 06) Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar.')

numero = int(input(f'\n\t Digite um número: '))

if numero % 2 == 0:
    print(f'\n\t O número {numero} é PAR.')
else:
    print(f'\n\t O número {numero} é ÍMPAR.')
