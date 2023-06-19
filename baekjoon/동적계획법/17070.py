import sys

input = sys.stdin.readline

N = int(input().strip())

house = [list(map(int, input().strip().split())) for _ in range(N)]
# 벽(1)에 닿으면 안된다
# 가로 : 가로, 대각선
# 세로 : 세로, 대각선
# 대가선 : 가로, 세로, 대각선

'''
즉, 
가로, 대각선-> 가로
세로, 대각선 -> 세로
가로, 세로, 대각선 -> 대각선
'''