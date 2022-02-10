N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
ans_list = list(map(int, input().split()))

for x in ans_list:
    start = 0
    end = N - 1
    temp = False
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == x:
            temp = True
            break
        elif num_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    if temp:
        print('1')
    else: print('0')
