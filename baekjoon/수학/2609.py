import sys, math

input = sys.stdin.readline


def lcm(a, b):
    return a * b // math.gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().strip().split())

    print(math.gcd(a, b))
    print(lcm(a, b))