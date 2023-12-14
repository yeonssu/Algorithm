import sys
input = sys.stdin.readline


if __name__ == "__main__":
    e, s, m = map(int, input().strip().split())
    now_e, now_s, now_m = 1, 1, 1
    answer = 1
    while True:
        if now_e == e and now_s == s and now_m == m:
            print(answer)
            break
        answer += 1
        now_e += 1
        now_s += 1
        now_m += 1
        if now_e > 15:
            now_e = 1
        if now_s > 28:
            now_s = 1
        if now_m > 19:
            now_m = 1
