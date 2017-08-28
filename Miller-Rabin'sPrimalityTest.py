#testing prime number
import random
import math
def prime(n,b):
    q = n-1
    abc = b
    rng = abc * math.log(q, 10)
    for a in range(1,rng):
        m = q; y = 1
        a = random.randrange(1,100)% q+1
        z = a
        while m > 0:
            while m % 2 is 0:
                x = z; z = z ** 2 % n
                if (z is 1) & (x != 1) & (x != q):
                    return False
                m = m/2
            m = m -1; y = (y * z) % n
        if y != 1:
            return False
    return True
getRandNo = random.randrange(1,100)
print(getRandNo)
prime(getRandNo, 4)
'''
getValue = prime(getRandNo, 4)
print(getValue)
'''