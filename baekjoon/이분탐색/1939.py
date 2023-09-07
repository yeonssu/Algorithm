import sys
from collections import defaultdict, deque

input = sys.stdin.readline


# 특정 무게를 factory1에서 factory2로 옮길 수 있는지 확인
def is_possible_to_move(start, end, weight):
    que = deque()
    que.append(start)
    visited = [False * (N + 1) for _ in range(N + 1)]
    visited[start] = True
    while que:
        now = que.popleft()
        for limit, next in bridge[now]:
            if not visited[next] and weight <= limit:
                visited[next] = True
                que.append(next)

    if visited[end]:
        return True
    else:
        return False


def binary_search(left, right):
    global answer
    while left <= right:
        mid = (left + right) // 2
        # 이동 가능 -> 중량을 늘려야 한다
        if is_possible_to_move(factory1, factory2, mid):
            answer = mid
            left = mid + 1
        # 이동 불가 -> 중량을 줄여야 한다
        else:
            right = mid - 1


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    bridge = defaultdict(list)
    for _ in range(M):
        A, B, C = map(int, input().strip().split())
        bridge[A].append((C, B))
        bridge[B].append((C, A))
    print(bridge)
    factory1, factory2 = list(map(int, input().strip().split()))
    answer = 0
    binary_search(1, 1000000000)
    print(answer)