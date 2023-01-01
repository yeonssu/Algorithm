# sol 1
a, b = map(int, input().split())

A = list(map(int,str(a)))
B = list(map(int,str(b)))

new_a = A[0] + A[1]*10 + A[2]*100
new_b = B[0] + B[1]*10 + B[2]*100

print(max(new_a, new_b))

# sol 2
a, b = input().split()
reversed_a = "".join(reversed(a))
reversed_b = "".join(reversed(b))

print(max(int(reversed_a), int(reversed_b)))
