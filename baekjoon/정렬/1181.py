import sys
input = sys.stdin.readline

words = list(set(input().strip() for _ in range(int(input().strip()))))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
