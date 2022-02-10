N = int(input())
n_arr = list(map(int, input().split()))
cnt = 0
def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for num in n_arr:
    if num > 1:
        if isPrime(num):
            cnt += 1
print(cnt)