import sys, math

input = sys.stdin.readline

T = int(input().strip())

for t in range(T):
    # n : 컴퓨터 개수 / d : 의존성 개수 / c : 해킹 당한 컴퓨터 번호
    n, d, c = map(int, input().strip().split())
    graph = [[math.inf] * (n + 1) for _ in range(n + 1)]
    print(graph)
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존
        # 컴퓨터 b가 감염 -> s초 후 컴퓨터 a도 감염됨
        a, b, s = map(int, input().strip().split())
