x = int(input('Informe um codigo (1,2,3) ou 4 para parar : '))

alcool = 0
gasolina = 0
diesel = 0

while x != 4 :
    if x == 1:
        alcool = alcool + 1
    elif x == 2:
        gasolina = gasolina + 1
    elif x == 3 :
        diesel = diesel + 1
    x = int(input('Informe um codigo (1,2,3) ou 4 para parar : '))

print('Muito obrigado')
print(f'Alcool : {alcool}')
print(f'Gasolina : {gasolina}')
print(f'Diesel : {diesel}')
    
    
