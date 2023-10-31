import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    answer = 0
    while n > 0:
        if n % 5 == 0:
            answer += n // 5
            n %= 5
            break
        else:
            n -= 2
            answer += 1

    if n == 0:
        print(answer)
    else:
        print(-1)
