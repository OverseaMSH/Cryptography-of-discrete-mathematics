import math

def fermat_factor(n):
    assert n % 2 != 0  # n must be odd
    a = math.ceil(math.sqrt(n))
    b2 = a*a - n
    while not is_square(b2):
        a += 1
        b2 = a*a - n
    b = int(math.sqrt(b2))
    return (a - b, a + b)

def is_square(n):
    root = int(math.isqrt(n))
    return n == root * root

# Example usage
n = 5959  # Example modulus
p, q = fermat_factor(n)
print(f"Factors of {n} are {p} and {q}")
