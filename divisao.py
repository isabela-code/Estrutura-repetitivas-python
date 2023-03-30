x = int(input('Quantos numeros voce vai digitar? '))

for i in range (0,x):
   y = int(input('Entre com o numerador : '))
   z = int(input('Entre com o denominador : '))
   if z!=0:
       divisao = y/z
       print(f'Divisão = {divisao : .2f}')
   else:
       print('Divisão impossivel')
        