a = eval(input('Length in centimeters:'))
if a < 0:
    print('The entry is invalid')
if a >= 0:
    print('Inch≈',round((a/2.54),2))
