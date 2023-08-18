import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = []
    words = list(map(str, input().strip()))
    for word in words:
        stack.append(word)
        if word == ")" and stack[len(stack) - 2] == "(":
            stack.pop()
            stack.pop()
    print("NO" if stack else "YES")
