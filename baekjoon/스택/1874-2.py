import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []
answer = []
i = 1
for _ in range(n):
    num = int(input().strip())
    while i <= num:
        stack.append(i)
        answer.append("+")
        i += 1

    if stack[len(stack) - 1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()

for i in answer:
    print(i)
