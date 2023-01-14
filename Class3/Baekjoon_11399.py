import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))
arr.sort()
tot = 0
for i in range(n):
    tot += int(arr[i]) * (n - i)

print(tot)

