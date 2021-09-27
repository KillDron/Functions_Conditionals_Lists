import random
A = random.randrange(1,11)
F = "не праві"
e = 0
while F == "не праві":
    if A == int(input("Ваше число:")):
        F = "праві"
        e += 1
        print("Цього разу ви були", F)
        print("Кількість спроб",e)
    else:
        print("Цього разу ви були", F)
        e += 1
