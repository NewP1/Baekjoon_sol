import sys
a, b = map(int, sys.stdin.readline().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x
print(gcd(max(a,b),min(a,b)))
print(round((a * b)/gcd(max(a,b),min(a,b))))
