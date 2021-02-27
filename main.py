import random


def miller_rabin(n, k):
    for i in range(0, k):
        a = int(random.random() * (n - 2))
        x = n - 1
        s = 0
        while x % 2 != 0:
            x /= 2
            s += 1
        r = (n - 1) / (2 ** x)
        x = a ** r
        if x % n == 1 or x % n == n - 1:
            continue
        else:
            j = 0
            while True:
                x = x ** 2
                if x % n == n - 1 or j >= s - 1:
                    break
                j += 1
            if j == s - 1:
                return False
    return True


print(miller_rabin(82589933, 50))
