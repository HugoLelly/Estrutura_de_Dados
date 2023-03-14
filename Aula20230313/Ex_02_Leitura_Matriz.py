# Universidade de Vassouras - Maricá
# Estrutura de Dados
# Márcio Garrido
# 202211182
# Hugo Lelly de Lima Marinho

# 02) Leitura de Matriz


matriz = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 1, 2, 2],
    [0, 0, 0, 2, 2, 2]
]

soma01 = matriz[0][0]+matriz[0][1]+matriz[0][2]+matriz[1][1]+matriz[2][0]+matriz[2][1]+matriz[2][2]
soma02 = matriz[0][1]+matriz[0][2]+matriz[0][3]+matriz[1][2]+matriz[2][1]+matriz[2][2]+matriz[2][3]
soma03 = matriz[0][2]+matriz[0][3]+matriz[0][4]+matriz[1][3]+matriz[2][2]+matriz[2][3]+matriz[2][4]
soma04 = matriz[0][3]+matriz[0][4]+matriz[0][5]+matriz[1][4]+matriz[2][3]+matriz[2][4]+matriz[2][5]
soma05 = matriz[1][0]+matriz[1][1]+matriz[1][2]+matriz[2][1]+matriz[3][0]+matriz[3][1]+matriz[3][2]
soma06 = matriz[1][1]+matriz[1][2]+matriz[1][3]+matriz[2][2]+matriz[3][1]+matriz[3][2]+matriz[3][2]
soma07 = matriz[1][2]+matriz[1][3]+matriz[1][4]+matriz[2][3]+matriz[3][2]+matriz[3][3]+matriz[3][2]
soma08 = matriz[1][3]+matriz[1][4]+matriz[1][5]+matriz[2][4]+matriz[3][3]+matriz[3][4]+matriz[3][2]
soma09 = matriz[2][0]+matriz[2][1]+matriz[2][2]+matriz[3][1]+matriz[4][0]+matriz[4][1]+matriz[4][2]
soma10 = matriz[2][1]+matriz[2][2]+matriz[2][3]+matriz[3][2]+matriz[4][1]+matriz[4][2]+matriz[4][3]
soma11 = matriz[2][2]+matriz[2][3]+matriz[2][4]+matriz[3][3]+matriz[4][2]+matriz[4][3]+matriz[4][4]
soma12 = matriz[2][3]+matriz[2][4]+matriz[2][5]+matriz[3][4]+matriz[4][3]+matriz[4][4]+matriz[4][5]
soma13 = matriz[3][0]+matriz[3][1]+matriz[3][2]+matriz[4][1]+matriz[5][0]+matriz[5][1]+matriz[5][2]
soma14 = matriz[3][1]+matriz[3][2]+matriz[3][3]+matriz[4][2]+matriz[5][1]+matriz[5][2]+matriz[5][3]
soma15 = matriz[3][2]+matriz[3][3]+matriz[3][4]+matriz[4][3]+matriz[5][2]+matriz[5][3]+matriz[5][4]
soma16 = matriz[3][3]+matriz[3][4]+matriz[3][5]+matriz[4][4]+matriz[5][3]+matriz[5][4]+matriz[5][5]

print(f'\tMatriz: \n\t{matriz[0]} \n\t{matriz[1]} \n\t{matriz[2]} \n\t{matriz[3]} \n\t{matriz[4]} \n\t{matriz[5]} \n\t')

print(f'Padrão 01: \n{matriz[0][0]}{matriz[0][1]}{matriz[0][2]}\n {matriz[1][1]}\n{matriz[2][0]}{matriz[2][1]}{matriz[2][2]}\tResultado: {soma01}\n')

print(f'Padrão 02: \n{matriz[0][1]}{matriz[0][2]}{matriz[0][3]}\n {matriz[1][2]}\n{matriz[2][1]}{matriz[2][2]}{matriz[2][3]}\tResultado: {soma02}\n')

print(f'Padrão 03: \n{matriz[0][2]}{matriz[0][3]}{matriz[0][4]}\n {matriz[1][3]}\n{matriz[2][2]}{matriz[2][3]}{matriz[2][4]}\tResultado: {soma03}\n')

print(f'Padrão 04: \n{matriz[0][3]}{matriz[0][4]}{matriz[0][5]}\n {matriz[1][4]}\n{matriz[2][3]}{matriz[2][4]}{matriz[2][5]}\tResultado: {soma04}\n')

print(f'Padrão 05: \n{matriz[1][0]}{matriz[1][1]}{matriz[1][2]}\n {matriz[2][1]}\n{matriz[3][0]}{matriz[3][1]}{matriz[3][2]}\tResultado: {soma05}\n')

print(f'Padrão 06: \n{matriz[1][1]}{matriz[1][2]}{matriz[1][3]}\n {matriz[2][2]}\n{matriz[3][1]}{matriz[3][2]}{matriz[3][3]}\tResultado: {soma06}\n')

print(f'Padrão 07: \n{matriz[1][2]}{matriz[1][3]}{matriz[1][4]}\n {matriz[2][3]}\n{matriz[3][2]}{matriz[3][3]}{matriz[3][4]}\tResultado: {soma07}\n')

print(f'Padrão 08: \n{matriz[1][3]}{matriz[1][4]}{matriz[1][5]}\n {matriz[2][4]}\n{matriz[3][3]}{matriz[3][4]}{matriz[3][5]}\tResultado: {soma08}\n')

print(f'Padrão 09: \n{matriz[2][0]}{matriz[2][1]}{matriz[2][2]}\n {matriz[3][1]}\n{matriz[4][0]}{matriz[4][1]}{matriz[4][2]}\tResultado: {soma09}\n')

print(f'Padrão 10: \n{matriz[2][1]}{matriz[2][2]}{matriz[2][3]}\n {matriz[3][2]}\n{matriz[4][1]}{matriz[4][2]}{matriz[4][3]}\tResultado: {soma10}\n')

print(f'Padrão 11: \n{matriz[2][2]}{matriz[2][3]}{matriz[2][4]}\n {matriz[3][3]}\n{matriz[4][2]}{matriz[4][3]}{matriz[4][4]}\tResultado: {soma11}\n')

print(f'Padrão 12: \n{matriz[2][3]}{matriz[2][4]}{matriz[2][5]}\n {matriz[3][4]}\n{matriz[4][3]}{matriz[4][4]}{matriz[4][5]}\tResultado: {soma12}\n')

print(f'Padrão 13: \n{matriz[3][0]}{matriz[3][1]}{matriz[3][2]}\n {matriz[4][1]}\n{matriz[5][0]}{matriz[5][1]}{matriz[5][2]}\tResultado: {soma13}\n')

print(f'Padrão 14: \n{matriz[3][1]}{matriz[3][2]}{matriz[3][3]}\n {matriz[4][2]}\n{matriz[5][1]}{matriz[5][2]}{matriz[5][3]}\tResultado: {soma14}\n')

print(f'Padrão 15: \n{matriz[3][2]}{matriz[3][3]}{matriz[3][4]}\n {matriz[4][3]}\n{matriz[5][2]}{matriz[5][3]}{matriz[5][4]}\tResultado: {soma15}\n')

print(f'Padrão 16: \n{matriz[3][3]}{matriz[3][4]}{matriz[3][5]}\n {matriz[4][4]}\n{matriz[5][3]}{matriz[5][4]}{matriz[5][5]}\tResultado: {soma16}\n')

