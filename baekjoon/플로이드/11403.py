import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input().strip())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]
    for middle in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1 or (graph[i][middle] == 1 and graph[middle][j] == 1):
                    graph[i][j] = 1

    for a in graph:
        print(*a)
