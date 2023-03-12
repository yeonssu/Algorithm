word = input()

result = ""
i = 0
while i < len(word):
    if word[i] == "<":
        while word[i] != ">":
            result += word[i]
            i += 1
        result += word[i]
        i += 1
    else:
        sub_word = ""
        while i <= len(word) - 1 and word[i] != " " and word[i] != "<":
            sub_word += word[i]
            i += 1
        result += sub_word[::-1]
        if i > len(word) - 1:
            break
        if word[i] != "<":
            result += word[i]
            i += 1

print(result)
