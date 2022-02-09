n = int(input())
score_list = list(map(int,input().split()))
score_max = max(score_list)
new_lsit = []

for score in score_list:
    new_lsit.append(score/score_max*100)
avg = sum(new_lsit)/n
print(avg)
