# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 06) Criar uma lista com números inteiros e verificar se um determinado número está na lista ou não.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 06) Criar uma lista com números inteiros e verificar se um determinado número está na lista ou não.')

lista = [9, 4, 23, 7, 8, 92, 3, 11]

numero_sim = 4

numero_nao = 5

print(f'\n\t Na lista: \n\t {lista} \n\t O numero: {numero_sim}.')

if numero_sim in lista:
    print(f'\t Está presente.')
else:
    print(f'\t Não está presente.')

print(f'\t O numero: {numero_nao}.')
if numero_nao in lista:
    print(f'\t Está presente.')
else:
    print(f'\t Não está presente.')
