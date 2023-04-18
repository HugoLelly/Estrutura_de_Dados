# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

#03) Escreva uma função que calcule o número de passos necessários para se chegar ao topo de uma montanha com n metros
#de altura, sabendo que cada passo dado aumenta a altitude em 10 centímetros e que um passo corresponde a 1 metro.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t03) Escreva uma função que calcule o número de passos necessários para se chegar ao \n\ttopo de uma montanha com n metros de altura, sabendo que cada passo dado aumenta a altitude \n\tem 10 centímetros e que um passo corresponde a 1 metro.')

def passos_para_o_topo(altura_em_metros):
    altura_em_centimetros = altura_em_metros * 100
    passos = altura_em_centimetros // 10
    if altura_em_centimetros % 10 != 0:
        passos += 1
    return print(f'\n\tPara chegar ao topo, será nescessario {passos} Passos.\n')

passos_para_o_topo(2000)
