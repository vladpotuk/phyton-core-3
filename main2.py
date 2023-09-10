import math
try:
    a=int(input('Довжина a:'))
    b=int(input('Ширина b:'))
    x=(a+b)*2
    print('Периметр прямокутника')
    print(x)

except Exception as ex:
    print (ex)

