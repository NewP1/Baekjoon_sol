import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1, 2]
if n < 3:
    print(arr[n])
else:
    for i in range(3, n+1):
        arr.append((arr[i-2] + arr[i-1]) % 10007)
    print(arr[n])

# for i in range(2, n+1):
#     b = i // 2
#     for j in range(0, b+1):
#         r = i - j
#         arr[i] += math.factorial(r) // (math.factorial(j) * math.factorial(r - j))
#     arr[i] = arr[i] % 10007