x = float(input('Digite a primeira nota : '))
while (x < 0 or x > 10):
    x = float(input('Valor invalido! Tente novamente : '))
    
y = float(input('Digite a segunda nota : '))
while (y < 0 or y > 10):
    y = float(input('Valor invalido! Tente novamente : '))

media = (x+y) /2
print(f'Media = {media}')