#prime no divisible by 1 and itself
import random
randNo = random.randrange(1,100)
print(randNo)
primeList = []
for num in range(2, randNo):
    isPrime = True
    for x in range(2, num):
        if num % x == 0:
             isPrime = False
             break
    if isPrime:
        primeList.append(num)
print(primeList)