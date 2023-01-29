import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1, 3]

if n < 3:
    print(arr[n])
else:
    for i in range(3, n+1):
        arr.append(((arr[i-2] * 2) + arr[i-1])%10007)
    print(arr[n])