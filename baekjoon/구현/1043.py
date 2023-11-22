import sys
from collections import defaultdict
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    trust = list(map(int, input().strip().split()))[1:]
    information = defaultdict(list)
    parties = []
    for _ in range(m):
        party = list(map(int, input().strip().split()))[1:]
        parties.append(party)
        for i in range(len(party)):
            information[party[i]].extend(party[:i] + party[i + 1:])

    visited = [False] * (n + 1)
    while trust:
        person = trust.pop()
        if not visited[person]:
            visited[person] = True
            same = information.get(person)
            if same is None:
                continue
            trust.extend(same)

    answer = 0
    for party in parties:
        for person in party:
            if visited[person]:
                break
        else:
            answer += 1
    print(answer)
