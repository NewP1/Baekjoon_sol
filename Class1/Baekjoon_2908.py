a, b = map(int, input().split())
num_list = []

num_list.append(int(str(a)[::-1]))
num_list.append(int(str(b)[::-1]))
print(max(num_list))