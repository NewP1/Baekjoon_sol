N, X = map(int, input().split())
nums = list(map(int, input().split()))
for x in nums:
    if x < X:
        print(x, end=" ")
