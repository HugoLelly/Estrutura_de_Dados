# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 05) Criar uma lista com números inteiros e contar quantos números pares e quantos números ímpares existem na lista.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 05) Criar uma lista com números inteiros e contar quantos números pares e quantos números ímpares existem na lista.')

lista = [9, 4, 23, 7,8, 92, 3, 11]
pares = 0
impares = 0

for numero in lista:
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f'\n\t Na lista {lista} existe \n\t {pares} números pares e \n\t {impares} números ímpares.')