import sys
from collections import deque

input = sys.stdin.readline


# D : 두 배로 바꾼다 (9999보다 크면 10000으로 나눈 나머지)
def d(num):
    return (num * 2) % 10000


# S : 1을 뺀다 (0이면 9999)
def s(num):
    return (num - 1) % 10000


# L : 맨 앞자리를 맨 뒤로 회전
def l(num):
    return (10 * num + (num // 1000)) % 10000


# R : 맨 뒷자리를 맨 앞으로 회전
def r(num):
    return (num // 10 + (num % 10) * 1000) % 10000


T = int(input().strip())
for t in range(T):
    a, b = map(int, input().strip().split())
    que = deque()
    que.append((a, ""))
    visited = [False for _ in range(10001)]

    while que:
        num, result = que.popleft()
        visited[num] = True
        if num == b:
            print(result)
            break

        num1 = d(num)
        if not visited[num1]:
            que.append((num1, result + "D"))
            visited[num1] = True

        num2 = s(num)
        if not visited[num2]:
            que.append((num2, result + "S"))
            visited[num2] = True

        num3 = l(num)
        if not visited[num3]:
            que.append((num3, result + "L"))
            visited[num3] = True

        num4 = r(num)
        if not visited[num4]:
            que.append((num4, result + "R"))
            visited[num4] = True
