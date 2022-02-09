N = 10
num_list = []
rem_list = []
for i in range(N):
    num_list.append(int(input()))

for num in num_list:
    temp = num % 42
    if rem_list.count(temp) == 0:
        rem_list.append(temp)
print(len(rem_list))