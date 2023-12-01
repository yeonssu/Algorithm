import sys
input = sys.stdin.readline


if __name__ == "__main__":
    answer = [0] * 10000
    for num in range(1, 10001):
        li = list(map(int, str(num)))
        num += sum(li)
        if num <= 10000:
            answer[num - 1] = 1

    for a in range(10000):
        if answer[a] == 0:
            print(a + 1)

