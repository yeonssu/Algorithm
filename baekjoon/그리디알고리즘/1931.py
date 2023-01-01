count = int(input())
array = [[0]*2 for i in range(count)]

for i in range(count):
    starting_time, finishing_time = map(int, input().split())
    array[i][0] += starting_time
    array[i][1] += finishing_time

array = sorted(array, key=lambda x: (x[1], x[0]))

result = 1
meeting = array[0]

for i in range(1, count):
    if array[i][0] < meeting[1]:
        continue
    else:
        result += 1
        meeting = array[i]

print(result)

