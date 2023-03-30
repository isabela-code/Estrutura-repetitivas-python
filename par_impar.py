x = int(input('Quantos numeros voce vai digitar? '))

for i in range (0,x):
    y = int(input('Digite um numero : '))
    if y < 0 and y%2!=0:
        print('Impar negativo')
    elif y < 0 and y%2== 0:
        print('Par negativo')
    elif y > 0 and y%2!=0:
        print('Impar positivo')
    elif y > 0 and y%2 == 0:
        print('Par positivo')
    else :
        print("Nulo")
