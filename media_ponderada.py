x = int(input('Quantos numeros voce vai digitar? '))

for i in range (0,x):
   print('Digite tres numeros :')
   y = float(input(''))
   z = float(input(''))
   w = float(input(''))
   media = ((y*2) + (z*3) + (w*5))/10
   print(f'Media = {media : .1f}')
   
