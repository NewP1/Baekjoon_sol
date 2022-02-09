own_num = list(map(int,input().split()))
tot = 0
for x in own_num:
    tot += x**2
num = tot%10
print(num)