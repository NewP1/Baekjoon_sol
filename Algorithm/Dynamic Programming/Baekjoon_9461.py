import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = [0, 1, 1, 1, 2, 2]
    n = int(input())
    if n < 6:
        print(arr[n])
    else:
        for i in range(6, n+1):
            arr.append(arr[i-5] + arr[i-1])
        print(arr[n])