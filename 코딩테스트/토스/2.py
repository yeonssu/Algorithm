# 뭐지? bfs?
from collections import defaultdict, deque


def solution(relationships, target, limit):
    answer = 0
    dic = defaultdict(list)
    n = 0
    for r in relationships:
        dic[r[0]].append(r[1])
        dic[r[1]].append(r[0])
        n = max(n, r[0], r[1])

    already = dic[target]
    answer += len(already) * 5

    que = deque()
    visited = [False] * (n + 1)
    visited[target] = True
    for a in already:
        que.append((1, a))
        visited[a] = True

    new = []
    while que:
        grade, friend = que.popleft()
        if grade == limit:
            break

        if dic[friend] is not None:
            for i in dic[friend]:
                if not visited[i]:
                    que.append((grade + 1, i))
                    new.append(i)
                    visited[i] = True

    answer += 10 * len(new) + len(new)
    return answer


solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 1, 2)
solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 2, 3)
