array = [[0]*9 for i in range(9)]

for i in range(9):
    array[i] = list(map(int, input().split()))

Max = array[0][0]
col = 0
row = 0

for i in range(9):
    for j in range(9):
        if array[i][j] > Max:
            Max = array[i][j]
            col = i
            row = j

print(Max)
print(col+1, row+1)