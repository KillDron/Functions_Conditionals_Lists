items=int(input('How many items are you buying?:'))
total=0
if 0<items<10:
    total = items*12
if 9<items<100:
    total = items*10
if items>99:
    total = items*7
print(total)
