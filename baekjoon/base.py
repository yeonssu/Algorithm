a, b = map(int, input().split())
max_value = max(a, b)
for i in reversed(range(1, max_value)):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(1, a * b):
    if i % a == 0 and i % b == 0:
        print(i)
        break
