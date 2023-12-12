import sys, math
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    print(math.comb(n, m))
