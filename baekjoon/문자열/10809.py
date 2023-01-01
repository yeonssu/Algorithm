word = input()

alpabet = 'abcdefghijklmnopqrstuvwxyz'
alpabet_len = len(alpabet)

for i in range(alpabet_len):
    result = word.find(alpabet[i])
    print(result, end=" ")