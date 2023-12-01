import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    if n == 1:
        print(1)
        exit()
    num = 2
    i = 1
    while True:
        before = num
        num += i * 6
        i += 1
        if before <= n < num:
            print(i)
            break
