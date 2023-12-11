import sys
input = sys.stdin.readline


def factorial(num):
    a = 1
    for i in range(1, num + 1):
        a *= i
    return list(map(int, str(a)))


if __name__ == "__main__":
    n = int(input().strip())
    answer = 0
    for i in reversed(factorial(n)):
        if i == 0:
            answer += 1
        else:
            print(answer)
            exit()
