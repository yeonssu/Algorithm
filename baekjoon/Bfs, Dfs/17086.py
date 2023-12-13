import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    farm = [list(map(int, input().strip().split())) for _ in range(n)]


