# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 03) Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, seguido do seu antecessor e do seu sucessor. 

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 03) Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, \n\t seguido do seu antecessor e do seu sucessor.')

numero = int(input(f'\n\t Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'\n\t Você digitou o número {numero}. \n\t Seu antecessor é {antecessor}. \n\t Seu sucessor é {sucessor}.')