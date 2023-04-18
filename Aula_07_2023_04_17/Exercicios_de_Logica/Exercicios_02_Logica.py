# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

#02) Escreva uma função que calcule o número de dias necessários para concluir um projeto, sabendo que o projeto tem n
#tarefas e cada tarefa leva d dias para ser concluída.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t02) Escreva uma função que calcule o número de dias necessários para concluir um projeto, \n\tsabendo que o projeto tem n tarefas e cada tarefa leva d dias para ser concluída.')

def tempo_do_projeto(numero_tarefas, dias_por_tarefa):
    tempo_total = numero_tarefas * dias_por_tarefa
    return print(f'\n\tO projeto será concluido em {tempo_total} dia.\n')

tempo_do_projeto(4, 2)
