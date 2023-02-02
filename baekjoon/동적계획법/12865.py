import sys

input = sys.stdin.readline
N, K = map(int, input().strip().split())

stuff = [[0, 0]]
for n in range(N):
    stuff.append(list(map(int, input().strip().split())))
bag = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            bag[i][j] = bag[i - 1][j]  # weight 보다 작으면 위의 값을 그대로 가져 온다
        else:
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])
print(bag[N][K])

'''
bag[i][j]
i:세로, 물건 / j:가로, 가방 최대 용량
만약 총 물건 수가 4개이고, 넣을 수 있는 최대 무게가 7일 경우
(이전 값들이 있어야 Index 를 넘지 않으므로 4+1, 7+1로 생성)
    
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 0
    
                      0 1 2 3 4 5  6  7
                      0 0 0 0 0 0  0  0
물건 무게 6, 가치 13짜리   0 0 0 0 0 0 13 13
물건 무게 4, 가치  8짜리   0 0 0 0 8 8 13 13
물건 무게 3, 가치  6짜리   0 0 0 6 8 8 13 14(6+8) 
물건 무게 5, 가치 12짜리   0 0 0 6 8 8 13 14(6+8)

현재 물건이 j보다 작으면 이전값 bag[i][j] = bag[i-1][j]
현재 물건이 j보다 크거나 같으면 두 개의 가치 중 큰 값
(이전값)과 (현재 물건의 가치 + 현재 물건을 넣지 않은 무게에 해당 하는 이전값)  
bag[i-1][j]         value + bag[i-1][j-weight]
'''
