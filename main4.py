try:
    a=int(input('Зарплата за місяць'))
    b=int(input('Місячний платіж за місяць'))
    d=(int(input('Заборгованність за комунальні платежі')))
    x=a-b-d
    print(x)

except Exception as ex:
    print(ex)