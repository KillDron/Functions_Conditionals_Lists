L = str(input("Запишіть числа через кому:")).split(sep=",")
Li = []
R = "NO"
c = 0
c2 = 0

print("Довжина списку:",len(L))

print("Останній елемент списку:",L[-1])

print("Список наоборот:",list(reversed(L)))

for i in L:
    Li.append(int(i))
    if int(i) == 5:
        R = "YES"
        c += 1
    elif int(i) < 5:
        c2 += 1
print("Чи є 5:",R)
print("Кількість 5:",c)


Li.pop(0)
Li.pop(-1)
print("Посортований список без першої і останньої цифри:",sorted(Li))

print("Кількість чисел менше 5:",c2)

