import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().split())
    arr = [0] * (n + 1)
    arr[1] = m
    for i in range(2, n + 1):
        arr[i] = (arr[i-1] * (m - (i - 1))) // i
    print(arr[n])
