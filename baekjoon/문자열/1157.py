# sol1)
normal_word = input()       # mississipi
upper_word = normal_word.upper() 
word_lst = list(set(upper_word)) # ['m', 'i', 's', 'p']

cnt = []

for i in word_lst:              # i = m,i,s,p
    count = upper_word.count(i)
    cnt.append(count)           # cnt=[1,4,4,1]

if cnt.count(max(cnt)) >= 2:    # max(cnt) = 4 / cnt.count(max(cnt)) = 2
    print("?")
else:     
    print(word_lst[cnt.index(max(cnt))])

# sol2)
normal_word = input()
upper_word = normal_word.upper() 
alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in upper_word:
    alphabet[ord(i)-65] += 1

if alphabet.count(max(alphabet)) >= 2:
    print("?")
else:     
    print(chr(alphabet.index(max(alphabet))+65))