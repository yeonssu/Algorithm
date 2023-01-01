N, M = map(int, input().split())

A = [[0]*M for i in range(N)]
B = [[0]*M for i in range(N)]
result_list = [[0]*M for i in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    B[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        result_list[i][j] = A[i][j] + B[i][j]

for i in result_list:
		for j in i:
				print(j, end=" ")
		print()