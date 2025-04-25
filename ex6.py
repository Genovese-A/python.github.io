"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hr = input('Qual é o horario: ')
minutos = input('Quantos minutos: ')
hora = (hr + ':' + minutos)
int_hr = int(hr) 
int_min = int(minutos)
try:
    if int_min <= 60:
        ...
    else:
        print('Digite minutos validos')
    if int_hr >= 0 and int_hr < 12:
        print(f'Bom Dia, agora são {hora}hr')
    if  int_hr >= 12 and int_hr < 18:
        print(f'Boa Tarde, agora são {hora}hr')
    if int_hr >= 18 and int_hr <= 23:
        print(f'Boa Noite, agora são {hora}hr')
except:
    print('Voce não digitou um numero')

    