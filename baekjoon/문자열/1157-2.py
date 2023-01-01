normal_word = input()
upper_word = normal_word.upper() 
alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in upper_word:
    alphabet[ord(i)-65] += 1

if alphabet.count(max(alphabet)) >= 2:
    print("?")
else:     
    print(chr(alphabet.index(max(alphabet))+65))