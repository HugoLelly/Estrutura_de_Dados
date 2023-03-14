# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 05) Desenvolva um programa que leia quatro notas e que apresente a média final.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 05) Desenvolva um programa que leia quatro notas e que apresente a média final.')

nota1 = float(input(f'\n\t Digite a 1ª nota: '))
nota2 = float(input(f'\n\t Digite a 2ª nota: '))
nota3 = float(input(f'\n\t Digite a 3ª nota: '))
nota4 = float(input(f'\n\t Digite a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média Final é: {media}')