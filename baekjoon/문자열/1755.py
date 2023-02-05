import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())

arr = []
for i in range(N, M + 1):
    a = list(str(i))
    word = ""
    for j in range(len(a)):
        if a[j] == "1": word += "one"
        if a[j] == "2": word += "two"
        if a[j] == "3": word += "three"
        if a[j] == "4": word += "four"
        if a[j] == "5": word += "five"
        if a[j] == "6": word += "six"
        if a[j] == "7": word += "seven"
        if a[j] == "8": word += "eight"
        if a[j] == "9": word += "nine"
        if a[j] == "0": word += "zero"
    arr.append([i, word])
arr.sort(key=lambda x: x[1])

for i in range(len(arr)):
    if i % 10 == 9:
        print(arr[i][0], end="\n")
    else:
        print(arr[i][0], end=" ")
