import math
CO=float(input('Comprimento do cateto oposto: '))
CA=float(input('Comprimento do cateto adjacente: '))
HI=math.hypot(CO, CA)
print('A hipotenusa é {:.2f}'.format(HI))