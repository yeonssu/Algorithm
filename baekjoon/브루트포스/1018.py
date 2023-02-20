N, M = map(int, input().split())
input_list = []
cnt_list = []

for _ in range(N):
    input_list.append(input())

for a in range(N - 7):
    for b in range(M - 7):
        start_w = 0
        start_b = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if input_list[i][j] != "W":
                        start_w += 1
                    else:
                        start_b += 1
                else:
                    if input_list[i][j] != "W":
                        start_b += 1
                    else:
                        start_w += 1

        cnt_list.append(start_w)
        cnt_list.append(start_b)
