remainder = []
for i in range(10):
    num = int(input())%42
    remainder.append(num)

print(len(set(remainder)))