repeat_num = int(input())
word_list = []
for i in range(repeat_num):
    word_list.append(input())

cnt = 0
for j in word_list:
    nst_word = list(j)
    a = 0
    new_list = []
    new_list.append(nst_word[0])
    for k in range(1,len(nst_word)):
        if nst_word[a] == nst_word[k]:
            a += 1
            continue
        else:
            a += 1
            new_list.append(nst_word[k])

    if len(new_list) == len(set(new_list)):
        cnt += 1

print(cnt)
