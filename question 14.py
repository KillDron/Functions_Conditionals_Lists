def sumDigits(n):
 
    sum = 0
    while (n != 0):
 
        sum = sum + int(n % 10)
        n = int(n/10)
 
    return sum
 
 
n = int(input("Write your 4-digit number:"))
print(sumDigits(n))
