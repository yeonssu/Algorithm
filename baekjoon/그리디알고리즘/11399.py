N = int(input())
P = list(map(int, input().split()))

total = 0

for i in range(N):
    a = min(P)
    total += a*(N-i)
    P.remove(a)

print(total)