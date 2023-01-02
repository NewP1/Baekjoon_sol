import sys
input = sys.stdin.readline

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

N = int(input())
fac_str = str(factorial(N))

cnt = 0
for i in range(len(fac_str) - 1, -1, -1):
    if fac_str[i] == '0':
        cnt += 1
    else:
        break
print(cnt)
