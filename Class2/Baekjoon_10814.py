import sys
N = int(input())
p_list= []
for i in range(N):
    t_age, t_name = map(str, sys.stdin.readline().split())
    p_list.append([int(t_age), t_name])

p_list.sort(key=lambda x:x[0])

for product in p_list:
    print(f"{product[0]} {product[1]}")


