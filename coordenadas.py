print('Digite os valores das coordenadas X e Y: ')
x = int(input(''))
y = int(input(''))

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    else :
        print('Q4')
    x = int(input(''))
    y = int(input(''))