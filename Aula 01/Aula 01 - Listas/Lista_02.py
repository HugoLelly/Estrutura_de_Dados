# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 02) Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 02) Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.')

lista1 = [9, 4, 23, 7]

lista2 = [8, 92, 3, 11]

lista3 = lista1 + lista2

lista3.sort()

print(f'\n\t Lista em oredem crescente \n\t {lista3}')