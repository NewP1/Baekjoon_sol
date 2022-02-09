K, N = map(int, input().split())
line_list = []
for i in range(K):
    line_list.append(int(input()))
low = 1
high = max(line_list)

while low <= high:
    mid = (low + high) // 2
    tot = 0
    for i in line_list:
        tot += i // mid
    if tot >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)