import sys
input = sys.stdin.readline


if __name__ == "__main__":
    a, b, c, d, e, f = map(int, input().strip().split())
    x = (c * e - b * f) // (a * e - b * d)
    y = (c * d - a * f) // (b * d - a * e)
    print(x, y)
