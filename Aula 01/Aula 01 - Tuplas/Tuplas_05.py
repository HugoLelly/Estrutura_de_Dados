# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 05) Criar uma tupla com números inteiros e contar quantos números pares e quantos números ímpares existem na tupla. 

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 05) Criar uma tupla com números inteiros e contar quantos números pares e quantos números ímpares existem na tupla.')

tupla = (2, 3, 8, 5, 6, 9, 1, 10, 4)

pares = 0
impares = 0

for num in tupla:
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1

print(f'\n\t Na Tupla {tupla} existe \n\t {pares} números pares e \n\t {impares} números ímpares.')