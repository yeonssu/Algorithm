N = int(input())
M = int(input())
S = input()

# 50점
# Pn = "IO"*N + "I"
#
# answer = 0
# for m in range(M):
#     if S[m] == "I":
#         if m + (2 * N + 1) < M:
#             if S[m:m + (2 * N + 1)] == Pn:
#                 answer += 1
#
# print(answer)

# 100점
answer, cnt, i = 0, 0, 0
while i < M:
    if S[i:i + 3] == "IOI":
        i += 2
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)
