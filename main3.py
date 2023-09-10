import math
try:
    a=float(input('Enter a:'))
    b = float(input('Enter b:'))
    x=(a/100*b)

    print('Відсоток від числа')
    print(x)

except Exception as ex:
    print(ex)

