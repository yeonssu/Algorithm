T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())

    Y, X = N % H, N // H + 1
    if Y == 0:
        Y, X = H, N // H

    print(Y * 100 + X)