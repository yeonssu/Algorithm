import sys
K = int(input())

directions = []
direct_len = []
for i in range(6):
    direct, len = map(int, sys.stdin.readline().strip().split())
    direct_len.append([direct,len])
    directions.append(direct)

value1 = [] # 가로값 (가장긴 가로선, 세로선앞, 세로선 뒤)
for i in range(1,3): # 방향 1,2 가로 중
    if(directions.count(i)==1): # 만약 방향이 하나만 나왔으면(가장 긴 가로선이면)
        value1.append(direct_len[directions.index(i)])  # 가장 긴 가로선
        
        # 앞과 다음값 인덱스
        front_value = directions.index(i)-1
        next_value = directions.index(i)+1
        # 범위를 벗어나면 맨앞은 맨뒤로, 맨뒤는 맨앞으로
        if next_value<0 : next_value = 5
        if front_value<0 : front_value = 5
        if next_value>5 : next_value = 0
        if front_value>5 : front_value = 0

        value1.append(direct_len[front_value])
        value1.append(direct_len[next_value])

value2 = [] # 세로값 (가장긴 세로선, 가로선앞, 가로선 뒤)
for i in range(3,5):
    if(directions.count(i)==1): # 만약 방향이 하나만 나왔으면(가장 긴 세로선이면)
        value2.append(direct_len[directions.index(i)])  # 가장 긴 세로선
        
        # 앞과 다음값 인덱스
        front_value = directions.index(i)-1
        next_value = directions.index(i)+1
        # 범위를 벗어나면 맨앞은 맨뒤로, 맨뒤는 맨앞으로
        if next_value<0 : next_value = 5
        if front_value<0 : front_value = 5
        if next_value>5 : next_value = 0
        if front_value>5 : front_value = 0

        value2.append(direct_len[front_value])
        value2.append(direct_len[next_value])

    
big = value1[0][1]*value2[0][1]
small = abs(value1[1][1]-value1[2][1])*abs(value2[1][1]-value2[2][1])

print((big-small)*K)