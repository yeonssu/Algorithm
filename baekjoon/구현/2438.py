import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(1, n + 1):
        print('*' * i)
