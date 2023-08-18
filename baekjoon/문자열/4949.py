import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    words = list(map(str, sentence))
    stack = []
    for word in words:
        if word == "(" or word == ")" or word == "[" or word == "]":
            stack.append(word)
        if (word == ")" and stack[len(stack) - 2] == "(") or (word == "]" and stack[len(stack) - 2] == "["):
            stack.pop()
            stack.pop()
    print("no" if stack else "yes")
