prim_valor = input('Digite um valor: ')
seg_valor = input('Digite outro valor: ')
int_prim_valor = int(prim_valor)
int_seg_valor = int(seg_valor)


if int_prim_valor > int_seg_valor:
    print('O primeiro valor é maior que o segundo'
          ,int_prim_valor,'>',int_seg_valor)
elif int_seg_valor > int_prim_valor:
    print('O segundo valor é maior que o primeiro'
          , int_seg_valor, '>',int_prim_valor)
elif int_prim_valor == int_seg_valor:
    print('Os valores são iguais'
          , int_prim_valor, '=', int_seg_valor)
else:
    print('Por favor digite algum numero.')
