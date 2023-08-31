import sys
input = sys.stdin.readline

n = int(input().strip())
num = [0]
for _ in range(n):
    num.append(int(input().strip()))

same = [0]
pop_list = [0]
answer = []
visited = [False] * (n + 1)
index = 1
i = 1
while i <= n and index <= n:
    if not visited[i]:
        same.append(i)
        answer.append("+")
        visited[i] = True
    if same[len(same) - 1] == num[index]:
        pop_list.append(same.pop())
        answer.append("-")
        index += 1
        i -= 2
    i += 1

for i in range(len(same)):
    if num[i] != same[i]:
        print("NO")
        exit()

for i in answer:
    print(i)
