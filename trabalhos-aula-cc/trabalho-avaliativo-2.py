num_dias_mes = int(input('Informe o número de dias do mês: '))
while num_dias_mes < 28 or num_dias_mes > 31:
    num_dias_mes = int(input('VALOR INVÁLIDO Informe o número de dias do mês: '))

num_dias_sem = int(input('Informe o dia da semana: '))
while num_dias_sem < 1 or num_dias_sem > 7:
    num_dias_sem = int(input('VALOR INVÁLIDO Informe o dia da semana: '))

x = 1
print('DOM SEG TER QUA QUI SEX SAB')
if num_dias_sem > 1:
    print(f'{(num_dias_sem-1) * "    "}', end='')
for x in range(1, num_dias_mes + 1): 
    print(f'{x:02}', end='  ')
    num_dias_sem += 1
    if num_dias_sem > 7:
        num_dias_sem = 1
        print()




    






    

        