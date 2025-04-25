"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite algum numero inteiro: ')
try:
    numero = int(numero)
    if numero % 2 == 0:
        print('O numero que você digitou é par:', numero)
    if numero % 2 != 0:
        print('O unmero que você digitou é impar:', numero)
except:
     print('Voce não digitou um numero ou nao digitou um numero inteiro')




