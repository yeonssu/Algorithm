import sys

input = sys.stdin.readline

king, stone, N = input().strip().split()
king_location = [ord(king[0]) - 64, int(king[1])]
stone_location = [ord(stone[0]) - 64, int(stone[1])]

move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for n in range(int(N)):
    m = input().strip()
    kx = king_location[0] + move[m][0]
    ky = king_location[1] + move[m][1]
    if 0 < kx <= 8 and 0 < ky <= 8:
        if kx == stone_location[0] and ky == stone_location[1]:
            sx = stone_location[0] + move[m][0]
            sy = stone_location[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                king_location = [kx, ky]
                stone_location = [sx, sy]
        else:
            king_location = [kx, ky]

print(chr(king_location[0] + 64) + str(king_location[1]))
print(chr(stone_location[0] + 64) + str(stone_location[1]))
