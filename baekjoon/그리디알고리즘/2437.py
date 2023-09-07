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
# 1 1 2 3 6 7 30
# [0,0] [1, 1]
# 1 : [0, 1]
# 1 1 : [0,1] + [2,3] -> [0,2]
# 1 1 2 : [0,2] + [2,4] -> [0,4]
# 1 1 2 3 : [0,4] + [3,7] -> [0,7]
# 1 1 2 6 : [0,7] + [6,13] -> [0,13]
# 1 1 2 3 6 7 : [0, 13] + [7,20] -> [0,20]
# 1 1 2 3 6 7 30 : [0,20] + [30,50] 만족 x
