import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
lecture = []
que = []

for n in range(N):
    S, T = map(int, input().strip().split())
    lecture.append([S, T])

lecture.sort()

heapq.heappush(que, lecture[0][1])
class_count = 1

for i in range(1, N):
    if que[0] > lecture[i][0]:
        heapq.heappush(que, lecture[i][1])
        class_count += 1
    else:
        heapq.heappop(que)
        heapq.heappush(que, lecture[i][1])

print(class_count)

'''
[[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]
가장 빠른 강의 종료시간
que 3
cnt = 1
--------------------------------
[2,4]는 같은 강의실에서 안됨
4 추가
que 3, 4
cnt 증가!!!

[3,5]은 [1,3]과 같은 강의실에서 됨
3 지우고 5 추가
que 4, 5

[4, 6]은 [2,4]와 같은 강의실에서 됨
4지우고 6추가
que 5, 6

[5, 7]은 [3, 5]와 같은 강의실에서 됨
5지우고 7추가
que 6, 7
'''

'''
1. que에 lecture의 가장 빠른 강의 종료시간 추가
cnt = 1
2. lecture의 다음 강의 시작시간이 큐에 있는 종료시간보다 작으면 새 강의실 추가
que에 종료시간 추가
cnt += 1
3. lecture의 다음 강의 시작시간이 큐에 있는 종료시간보다 크거나같으면 이어서 가능
que에 있는 시간 빼고
que에 종료시간 추가    
'''




