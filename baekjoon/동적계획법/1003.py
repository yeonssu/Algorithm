import sys
input = sys.stdin.readline


def fibonacci(num):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if num >= 3:
        for i in range(3, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])


if __name__ == "__main__":
    for _ in range(int(input().strip())):
        fibonacci(int(input().strip()))
