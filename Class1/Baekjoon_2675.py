cnt = int(input())
num_list = []
s_list = []

for i in range(cnt):
    num, s = map(str, input().split())
    num_list.append(num)
    s_list.append(s)

for i in range(cnt):
    for cha in s_list[i]:
        print(cha * int(num_list[i]), end='')
    print()