import matplotlib.pyplot as plt

def gcd_count(a, b, count=0):
    if b == 0:
        return count
    return gcd_count(b, a % b, count + 1)

N = 5000
max_calls = [0] * (N + 1)  # Initialize list to store maximum calls for each a

# For each a, find the b that requires the most recursive calls
for a in range(N + 1):
    # Only need to check b values up to a
    for b in range(a + 1):
        calls = gcd_count(a, b)
        max_calls[a] = max(max_calls[a], calls)

# Plot the results
plt.plot(max_calls, '.')
plt.xlabel('a')
plt.ylabel('Maximum number of recursive calls')
plt.title('GCD Algorithm Complexity')
plt.show()
