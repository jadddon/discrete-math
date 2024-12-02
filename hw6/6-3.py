# 5.1 
import matplotlib.pyplot as plt

def gcd_call_total(a, b, total=0):
    if b == 0:
        return total
    return gcd_call_total(b, a % b, total+1)

print(gcd_call_total(64,32))

# 5.2 
N = 5000
call_upper_limit = [0]*(N+1)

for a in range(N+1):
    for b in range(a+1):
        call_total = gcd_call_total(a,b)
        call_upper_limit[a] = max(call_upper_limit[a], call_total)
plt.plot(call_upper_limit,'.')

# 5.3

def successive_fib(x):
    fib = [0,1]
    for i in range(2,x+1):
        fib += [fib[i-1]+fib[i-2]]
    return fib

gen_fib = successive_fib(100)

call_total = [gcd_call_total(gen_fib[i], gen_fib[i - 1]) for i in range(1, 101)]


plt.plot(range(1,101), call_total, '.')
