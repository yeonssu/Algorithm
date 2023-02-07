expression = list(input().split("-"))

num = []
for i in expression:
    if i.isdigit():
        num.append(int(i))
    else:
        sub = map(int, i.split("+"))
        num.append(sum(sub))

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)
