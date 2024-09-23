import math
an=float(input('Digite o angulo: '))
seno=math.sin(math.radians(an))
print('O angulo do {} tem seno de: {:.2f}'.format(an, seno))
coseno=math.cos(math.radians(an))
print('O angulo de {} tem o coseno de: {:.2f}'.format(an, coseno))
tangente=math.tan(math.radians(an))
print('O angulo de {} tem a tangente de: {:.2f}'.format(an, tangente))