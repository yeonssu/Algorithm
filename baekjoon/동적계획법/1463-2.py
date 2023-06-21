import sys, math

input = sys.stdin.readline

N = int(input())
array = [0, 0, 1, 1]

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    for i in range(4, N + 1):
        if i % 3 == 0:
            a = array[i // 3]
        else:
            a = math.inf

        if i % 2 == 0:
            b = array[i // 2]
        else:
            b = math.inf

        c = array[i - 1]

        array.append(1 + min(a, b, c))
    print(array[N])
