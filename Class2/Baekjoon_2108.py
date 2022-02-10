from collections import Counter
N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))
n_list.sort()


print(round(sum(n_list)/N))
print(n_list[int((N-1)/2)])

cnt = Counter(n_list).most_common(2)
if len(n_list) > 1:
    if cnt[0][1] == cnt [1][1]:
        print(cnt[1][0])
    else: print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(n_list)-min(n_list))

