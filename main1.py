import math
try:


    a=float(input('Enter a:'))
    b=float(input('Enter b:'))
    x1=a+b
    x2=a-b
    x3=a*b
    x4=a/b
    print(x1)
    print(x2)
    print(x3)
    print(x4)

except Exception as ex:
    print(ex)