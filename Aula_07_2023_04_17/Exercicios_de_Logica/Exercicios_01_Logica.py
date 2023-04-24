# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

#01) Escreva uma função que calcule o tempo necessário para cozinhar um ovo, sabendo que o tempo de cozimento para um
#ovo de tamanho médio é de 3 minutos e que cada ovo adicionado aumenta o tempo em 1 minuto.

print(f'\n\tUniversidade de Vassouras - Maricá \n\tEstrutura de Dados - Márcio Garrido \n\t202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t01) Escreva uma função que calcule o tempo necessário para cozinhar um ovo, \n\tsabendo que o tempo de cozimento para um ovo de tamanho médio é de \n\t3 minutos e que cada ovo adicionado aumenta o tempo em 1 minuto.')

def tempo_de_cozimento(numero_ovos):
    tempo_base = 3
    tempo_total = tempo_base + (numero_ovos - 1)
    return print(f'\n\tO tempo total de cozimento é de {tempo_total} minutos.\n')

tempo_de_cozimento(3)




