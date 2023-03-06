# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 07) Criar uma lista com nomes de frutas e verificar se uma determinada fruta está na lista ou não.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 07) Criar uma lista com nomes de frutas e verificar se uma determinada fruta está na lista ou não.')

frutas = ["Maçã", "Banana", "Melancia", "Abacaxi", "Goiaba"]

fruta_sim = "Banana"

fruta_nao = "Pera"

print(f'\n\t Na lista: \n\t {frutas} \n\t A {fruta_sim}.')

if fruta_sim in frutas:
    print(f'\t Está na lista.')
else:
    print(f'\t Não está na lista.')

print(f'\t A {fruta_nao}.')
if fruta_nao in frutas:
    print(f'\t Está na lista.')
else:
    print(f'\t Não está na lista.')