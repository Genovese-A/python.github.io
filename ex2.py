nome = 'Lucas'
altura = 1.70
peso = 60.20
imc = peso/(altura ** 2)

imc_2casa = f'{imc:.2f}'

print(nome, 'tem ',altura, 'de altura.')
print('pesa ',peso,'Kg e seu IMC é: ')
print(imc_2casa )