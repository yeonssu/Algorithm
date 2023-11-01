import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    pattern = input().strip()
    front = ""
    end = ""
    for i in range(len(pattern)):
        if pattern[i] == "*":
            front = pattern[:i]
            end = pattern[i + 1:]
    print(front)
    print(end)
    for _ in range(n):
        word = input().strip()
        print(word[:len(front)])
        print(word[-len(end):])
        if len(word) >= len(front) + len(end) and front == word[:len(front)] and end == word[-len(end):]:
            print("DA")
        else:
            print("NE")
