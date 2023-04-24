# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

#04) Escreva uma função que calcule o número de dias necessários para percorrer uma distância de d quilômetros, sabendo
#que cada dia o viajante percorre p quilômetros e que ele precisa descansar a cada x dias percorridos.

print(f'\n\tUniversidade de Vassouras - Maricá \n\tEstrutura de Dados - Márcio Garrido \n\t202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 04) Escreva uma função que calcule o número de dias necessários para percorrer uma \n\tdistância de d quilômetros, sabendo que cada dia o viajante percorre p quilômetros \n\te que ele precisa descansar a cada x dias percorridos.')

def tempo_de_viagem(distancia_em_km, quilometros_por_dia, dias_de_descanso):
    dias_de_viagem = distancia_em_km // quilometros_por_dia
    if distancia_em_km % quilometros_por_dia != 0:
        dias_de_viagem += 1
    dias_de_descanso_extra = dias_de_viagem // dias_de_descanso
    dias_de_viagem_total = dias_de_viagem + dias_de_descanso_extra
    return print(f'\n\tA viajem terá a duração de {dias_de_viagem_total} dias.\n')

tempo_de_viagem(8000, 1000, 8)
