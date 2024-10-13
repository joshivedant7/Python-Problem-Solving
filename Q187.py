#  Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
#  The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a  divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b)

x = int(input('Enter number : '))
y = int(input('Enter number : '))

def gcd(n,m):
    if m == 0:
        return n
    return gcd(m, n % m)

print(f"GCD({x},{y}) = {gcd(x,y)}")