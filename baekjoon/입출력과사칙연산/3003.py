want = [1, 1, 2, 2, 2, 8]
before = list(map(int,input().split()))
result = []

for i in range(6):
    if before[i] != want[i]:
        result.append(want[i] - before[i])
    else :
        result.append(0)

print(*result)