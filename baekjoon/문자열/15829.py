L = int(input())
r = 31
M = 1234567891
word = list(input())
result = 0

for i in range(L):
    result += (ord(word[i])-96)*(r**i)

print(result%M)