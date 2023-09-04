import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    weight = list(map(int, input().strip().split()))
    weight.sort()
    now_start = 0
    now_end = 0

    for w in weight:
        next_start = now_start + w
        next_end = now_end + w
        if now_end + 1 >= next_start:
            now_end = next_end
        else:
            break
    print(now_end + 1)
