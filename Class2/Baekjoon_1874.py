N = int(input())
num_list = []
op = []
cnt = 1
ans = True
for i in range(N):
    num = int(input())
    while cnt <= num:
        num_list.append(cnt)
        op.append('+')
        cnt += 1
    if num_list[-1] == num:
        num_list.pop()
        op.append('-')
    else:
        ans = False
        break
if ans == False:
    print('NO')
else:
    for i in op:
        print(i)


