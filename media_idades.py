print('Digite as idades : ')
x = int(input(''))
soma = 0 
y = 0
    
if x < 0 :
    print('Impossivel de calcular')
    
while x >= 0:
    soma = soma + x
    y = y + 1
    x = int(input(''))
media = soma/y
print(f"Media = {media : .2f}")

    