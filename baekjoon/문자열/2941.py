import sys

input = sys.stdin.readline

word = input().strip()
answer = 0
i = 0
while i < len(word):
    if i + 1 < len(word):
        sub = word[i:i + 2]
        if sub == "c=" or sub == "c-" or sub == "d-" or sub == "lj" or sub == "nj" or sub == "s=" or sub == "z=":
            i += 1

    if word[i] == "d" and i + 2 < len(word):
        sub = word[i:i + 3]
        if sub == "dz=":
            i += 2

    answer += 1
    i += 1

print(answer)
