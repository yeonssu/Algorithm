import sys

input = sys.stdin.readline


def calculate(m, n, x, y):
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().strip().split())
        print(calculate(M, N, x, y))
