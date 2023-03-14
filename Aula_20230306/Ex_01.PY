# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 01) Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro.

print(f'\n\t Universidade de Vassouras - Maricá \n\t Estrutura de Dados - Márcio Garrido \n\t 202211182 - Hugo Lelly de Lima Marinho')
print(f'\n\t 01) Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro.')


import datetime

data_atual = datetime.date.today()

data_futura = data_atual + datetime.timedelta(days=2)

print(f'\n\t A data atual é {data_atual}. \n\t A data futura é {data_futura}.')