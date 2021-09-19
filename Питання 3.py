import random
A = random.randrange(1,11)
F = "Не праві"
e = 0
print(A)
while F == "Не праві":
    if A == int(input("Ваше число:")):
        F = "Правий"
        e += 1
        print("Цього разу ви були", F)
        print("Кількість спроб",e)
    else:
        print("Цього разу ви були", F)
        e += 1
