import sys

''' 최소 신장 트리
- Kruskal
    - https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
    - 간선들을 정렬
    - 간선이 잇는 두 정점의 root를 찾는다.
    - 다르다면 하나의 root를 바꾸어 연결 시켜준다.
- Prim
    - 임의의 정점을 선택
    - 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
    - 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
'''
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

root = [i for i in range(N + 1)]
line = []
for _ in range(M):
    line.append(list(map(int, input().split())))

line.sort(key=lambda x: x[2])


# 사이클이 형성 되는지 확인
# Union-find | https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


answer = 0
for a, b, c in line:
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if a_root > b_root:
            root[a_root] = b_root
        else:
            root[b_root] = a_root
        answer += c

print(answer)
