word = input().upper()
spell = list(set(word))
cnt_list = []

for x in spell:
    cnt = list(word).count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(spell[cnt_list.index(max(cnt_list))])