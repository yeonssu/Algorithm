import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    if n == 0:
        print(0)
        exit()
    solved = [int(input().strip()) for _ in range(n)]
    solved.sort()
    # 파이썬 round 함수 : 0.5 초과 시 올림
    cut = round(n * 0.15 + 0.0000001)
    print(round(sum(solved[cut:len(solved) - cut]) / (n - cut * 2) + 0.0000001))
