# 5.1 
import matplotlib.pyplot as plt

def gcd_call_total(a, b, total=0):
    if b == 0:
        return total
    return gcd_call_total(b, a % b, total+1)

print(gcd_call_total(64,32))