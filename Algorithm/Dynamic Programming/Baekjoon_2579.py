import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)
if n == 1:
    print(int(input()))
else:
    for i in range(1, n+1):
        arr[i] = int(input())

    tot_list = [0] * (n+1)
    tot_list[1] = arr[1]
    tot_list[2] = tot_list[1] + arr[2]

    for i in range(3, n+1):
        tot_list[i] = max(arr[i] + tot_list[i-2], arr[i] + tot_list[i-3] + arr[i-1])
    print(tot_list[n])
