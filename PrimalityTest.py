#testing prime number
import random
def prime(n,b):
    q = n-1
    for a in range(1,100):
        m = q; y = 1
        a = random.randrange(1,100)% q+1
        z = a
        while m > 0:
            while m % 2 is 0:
                z = z ** 2 % n
                m = m/2
            m = m -1; y = (y * z) % n
        if y != 1:
            return False
    return True
getRandNo = random.randrange(1,100000000)
print(getRandNo)
getValue = prime(getRandNo, 4)
print(getValue)