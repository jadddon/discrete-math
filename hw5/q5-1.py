import random
from Crypto.Util import number

# Generate two 1024-bit primes
p = number.getPrime(1024)
q = number.getPrime(1024)

# Fermat primality test
def fermat_primality_test(n, k=10):
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Test both primes
p_is_prime = fermat_primality_test(p)
q_is_prime = fermat_primality_test(q)

print(f"Prime p: {p}")
print(f"Prime q: {q}")
print(f"Is p prime? {p_is_prime}")
print(f"Is q prime? {q_is_prime}")