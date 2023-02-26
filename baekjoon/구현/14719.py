import sys

input = sys.stdin.readline

H, W = map(int, input().strip().split())
block = list(map(int, input().strip().split()))
answer = 0
for want_height in range(H):
    want_height_index = []
    next_height_index = []

    i = 0
    while i < W:
        if block[i] == want_height:
            start = i
            end = i
            while 0 <= i + 1 < W and block[i + 1] == want_height:
                i += 1
                end = i
            want_height_index.append((start, end))
        i += 1

    for start, end in want_height_index:
        left = start - 1
        right = end + 1
        if 0 <= left < W and 0 <= right < W and block[left] > want_height and block[right] > want_height:
            for i in range(start, end + 1):
                answer += 1
                block[i] += 1

print(answer)
