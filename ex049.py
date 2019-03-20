n1 = int(input('enter with the integer number: '))
print('The multiplication table of {} is'.format(n1))
for i in range(0, 11):
    print('{} x {} = {}'.format(n1, i, n1*i))
