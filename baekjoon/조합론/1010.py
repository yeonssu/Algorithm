import sys, math
input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        print(math.comb(m, n))
