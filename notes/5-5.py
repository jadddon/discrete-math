# simple euclidean algorithm for computing gcd of two non-negative ints

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(40,10))


# extended euclidean algorithm

# Given a and b, return (gcd(a,b), x, y) s.t. ax+by = gcd(a,b)
def egcd(a,b):
    if b == 0:
        return a, 1, 0
    gcd, xp, yp = egcd(b, a % b)
    x = yp 
    y = xp - (a//b)*yp
    print("egcd(",b,",",a%b,")","-> (",gcd,",",xp,",",yp,")")
    return gcd, x, y


egcd(431,29)