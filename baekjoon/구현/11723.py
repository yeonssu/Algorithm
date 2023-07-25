import sys

input = sys.stdin.readline

M = int(input().strip())
arr = []

for m in range(M):
    sub = list(map(str, input().strip().split()))
    if len(sub) == 2:
        a = sub[0]
        b = int(sub[1])
    else:
        a = sub[0]
        b = 0

    if a == "add":
        if arr.count(b) > 0:
            continue
        else:
            arr.append(b)
    elif a == "remove":
        if arr.count(b) > 0:
            arr.remove(b)
        else:
            continue
    elif a == "check":
        if arr.count(b) > 0:
            print(1)
        else:
            print(0)
    elif a == "toggle":
        if arr.count(b) > 0:
            arr.remove(b)
        else:
            arr.append(b)
    elif a == "all":
        arr = list(range(1, 21))
    elif a == "empty":
        arr = []
