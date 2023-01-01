remember_word = list(input())

len_word = len(remember_word)
for i in range(len_word):
    if remember_word[i] == "A" or remember_word[i] == "B" or remember_word[i] == "C":
        remember_word[i] = "2"
    elif remember_word[i] == "D" or remember_word[i] == "E" or remember_word[i] == "F":
        remember_word[i] = "3"
    elif remember_word[i] == "G" or remember_word[i] == "H" or remember_word[i] == "I":
        remember_word[i] = "4"
    elif remember_word[i] == "J" or remember_word[i] == "K" or remember_word[i] == "L":
        remember_word[i] = "5"
    elif remember_word[i] == "M" or remember_word[i] == "N" or remember_word[i] == "O":
        remember_word[i] = "6"
    elif remember_word[i] == "P" or remember_word[i] == "Q" or remember_word[i] == "R" or remember_word[i] == "S":
        remember_word[i] = "7"
    elif remember_word[i] == "T" or remember_word[i] == "U" or remember_word[i] == "V":
        remember_word[i] = "8"
    elif remember_word[i] == "W" or remember_word[i] == "X" or remember_word[i] == "Y" or remember_word[i] == "Z":
        remember_word[i] = "9"
answer = 0
for j in remember_word:
    answer += int(j) + 1

print(answer)