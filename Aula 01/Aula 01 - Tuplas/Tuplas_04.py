# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 04) Remover todas as ocorrências de um determinado número de uma tupla de números inteiros. 

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 04) Remover todas as ocorrências de um determinado número de uma tupla de números inteiros.')

Tupla = (1,2,1,4,1,3,1,5,6,1,9,1)

numero = 1

nova_tupla = tuple(i for i in Tupla if i != numero)

print(f'\n\t Removido o numero 1 da Tupla: \n\t {Tupla} \n\t O resultado foi: \n\t {nova_tupla}')