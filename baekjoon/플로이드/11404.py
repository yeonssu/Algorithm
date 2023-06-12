import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
city = [[987654321] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    city[a][b] = min(city[a][b], c)

for middle in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                city[i][j] = 0
            else:
                if i != middle and j != middle:
                    city[i][j] = min(city[i][j], city[i][middle] + city[middle][j])

for row in city[1:]:
    for col in row[1:]:
        if col == 987654321:
            print(0, end=" ")
        else:
            print(col, end=" ")
    print()
