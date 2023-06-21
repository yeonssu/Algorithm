import sys

input = sys.stdin.readline

N = int(input())

# 1 -> 0번
# 2 -> (2) 1 -> 1번
# 3 -> (1) 1 -> 1번
# 4 -> (2) 2 -> (2) 1 -> 2번(a2 + 1)
# 5 -> (3) 4 -> (2) 2 -> (2) 1 -> 3번 (a4 + 1)
# 6 -> (1) 2 -> (2) 1 -> 2번 (a2 + 1)
# ...
# 그럼 an = min(a(n//2), a(n//3), a(n-1)) + 1 ???

array = [0] * (10 ** 6 + 2)
array[2] = 1
array[3] = 1
array[10 ** 6 + 1] = 999999999
# array = [0, 0, 1, 1]

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    for i in range(4, N + 1):
        if i % 3 == 0:
            a = i // 3
        else:
            a = 10 ** 6 + 1

        if N % 2 == 0:
            b = i // 2
        else:
            b = 10 ** 6 + 1

        c = i - 1

        array[i] = 1 + min(array[a], array[b], array[c])
    print(array[N])
