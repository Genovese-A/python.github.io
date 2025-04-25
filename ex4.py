nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é:', nome[-1::-1])
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('Seu nome NÃO tem espaço')
    print('O seu nome tem:',len(nome),'letras')
    print('A primeira letra do seu nome é:', nome[0])
    print('A ultima letra do seu nome é:', nome[-1])
else:
    print('Desculpe, mas voce deixou campos vazios.')
