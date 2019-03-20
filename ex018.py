from math import cos, sin, tan, radians
a = float(input('Enter with a angle: '))
ar = radians(a)
print('the cosine of {} is {:.2f}'.format(a, cos(ar)))
print('the sine of {} is {:.2f}'.format(a, sin(ar)))
print('the tangent of {} is {:.2f}'.format(a, tan(ar)))
