COUNT = int(input())

for k in range(COUNT):
    cnt = 0
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    temp = M
    while len(num_list) > 0:
        if num_list[0] != max(num_list):
            num_list.append(num_list[0])
            del num_list[0]
            if temp - 1 >= 0:
                temp -= 1
            else: temp = len(num_list) - 1
        else:
            if temp == 0:
                del num_list[0]
                cnt += 1
                break
            else:
                del num_list[0]
                temp -= 1
                cnt += 1
    print(cnt)