x = int(input('Quantos numeros voce vai digitar? '))

dentro = 0
fora = 0

for i in range (0,x):
    y = int(input('Digite um numero : '))
    if y < 10 or y > 20:
        fora = fora + 1
    else :
        dentro = dentro + 1

print(f'{dentro} dentro')
print(f'{fora} fora')