import sys
input = sys.stdin.readline
import math

n = int(input())

arr = [i for i in range(n+1)]

if n < 4:
    print(arr[n])
else:
    for i in range(4, n+1):
        for j in range(int(math.sqrt(i)), 1, -1):
            if arr[i] > arr[i - pow(j,2)] + 1:
                arr[i] = arr[i - pow(j,2)] + 1

    print(arr[n])
