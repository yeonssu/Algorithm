# sol 1
N, X = map(int, input().split())

num = list(map(int, input().split()))

for i in num:
    if i < X:
        print(i, end = " ")

# sol 2
N, X = map(int, input().split())

num = list(map(int, input().split()))

for i in range(N):
    if num[i] < X:
        print(num[i], end = " ")