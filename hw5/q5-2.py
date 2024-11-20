import math

# Compute ϕ = (p-1)(q-1)
phi = (p - 1) * (q - 1)

# Public key
e = 65537

# Verify gcd(e, ϕ) = 1
gcd_value = math.gcd(e, phi)

print(f"ϕ: {phi}")
print(f"gcd(e, ϕ): {gcd_value}")
print(f"Is gcd(e, ϕ) = 1? {gcd_value == 1}")