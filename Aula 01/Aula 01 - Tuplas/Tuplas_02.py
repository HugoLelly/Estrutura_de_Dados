# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 02) Criar duas tuplas de números inteiros e mesclá-las em uma terceira tupla em ordem crescente.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 02) Criar duas tuplas de números inteiros e mesclá-las em uma terceira tupla em ordem crescente.')

tupla_1 = (9, 4, 23, 7, 8)

tupla_2 = (92, 3, 11, 1, 65)

tupla_3 = tupla_1 + tupla_2
tupla_3 = sorted(tupla_3)

print(tupla_3)
print(f'\n\t As tuplas {tupla_1} e {tupla_2} \n\t Juntas em ordem cresente é: {tupla_3}')
