import math 

input = input()

if input[0] == ' ':
    input = input[1:]

a, b, c = input.split(' ')
a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - (4 * a * c)
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)

    print('R1 = {:0.5f}'.format(r1))
    print('R2 = {:0.5f}'.format(r2))