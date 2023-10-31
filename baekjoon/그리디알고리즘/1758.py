import sys
input = sys.stdin.readline


if __name__ == '__main__':
    tips = [int(input().strip()) for _ in range(int(input()))]
    tips.sort(reverse=True)
    answer = 0
    for i in range(len(tips)):
        if tips[i] - i > 0:
            answer += tips[i] - i
    print(answer)
