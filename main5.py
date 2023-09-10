try:
    a=int(input('Діагональ 1 '))
    b=int(input('Діагональ 2 '))
    x=1/2*a*b
    print('Площа ромба ')
    print(x)
except Exception as ex:
    print(ex)
