word = input()
danger = input()

stack = []
for i in range(len(word)):
    stack.append(word[i])
    if "".join(stack[-len(danger):]) == danger:
        for j in range(len(danger)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
