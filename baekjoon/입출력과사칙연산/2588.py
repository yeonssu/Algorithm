a = int(input())
b = int(input())
b = list(map(int, str(b)))

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))

print(a*int(b[2]) + 10*a*int(b[1]) + 100*a*int(b[0]))