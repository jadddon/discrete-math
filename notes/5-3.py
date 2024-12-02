# example 1

# Compute a^b mod n
def modexp(a,b,n):
    result = 1
    for i in range(b):
        result = (result * a) % n
    return result 

x1 = modexp(572,29,713)
print(x1)


# example 2 -- more efficient version using squaring

def modexp(a,b,n):
    res = 1
    while b > 0:
        if b%2 == 1:
            res = (res*a)%n
        a = (a*a)%n
        b = b//2        # b//2 = floor(b/2)
        print(res, "*", a, "^", b, " mod", n)
    return res

x2 = modexp(572, 29, 713)


# example 3 -- can just use pow() method in Python instead of formula

x3 = pow(572, 29, 713)
print(x3)

# example 4 -- use pow to find modular multiplicative inverses -- set exponent to -1

inv = pow(572, -1, 713)
print(inv)
print((572*inv)%713)