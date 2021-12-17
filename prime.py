def is_prime(n):
    x = int(n ** (1 / 2))
    for i in range(2, x + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
x = is_prime(n)
if x and n != 1:
    print(f"{n} is a prime number")
else:
    print(f"{n} isn't a prime number")
