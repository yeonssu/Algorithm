word = input()
danger = input()

while danger in word:
    word = word.replace(danger, "")

if len(word) == 0:
    print("FRULA")
else:
    print(word)
