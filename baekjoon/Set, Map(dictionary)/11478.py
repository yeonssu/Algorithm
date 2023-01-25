S = input()
num = len(S)
S_set = set()

for i in range(num):
    for j in range(num-i):
        S_set.add(S[j:j+i+1])

print(len(S_set))