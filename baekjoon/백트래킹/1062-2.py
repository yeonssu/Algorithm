import sys
from itertools import combinations
from string import ascii_lowercase

input = sys.stdin.readline

N, K = map(int, input().strip().split())
words = [input().strip()[4:-4] for _ in range(N)]
alphabet = set(ascii_lowercase) - {'a', 'n', 't', 'i', 'c'}
answer = 0
if K - 5 < 0:
    print(0)
else:
    teach_letter = [False] * 123
    for letter in ["a", "n", "t", "i", "c"]:
        teach_letter[ord(letter)] = True

    for combi in combinations(alphabet, K - 5):
        for letter in list(combi):
            teach_letter[ord(letter)] = True

        cnt = 0
        for word in words:
            read = True
            for w in word:
                if not teach_letter[ord(w)]:
                    read = False
                    break
            if read:
                cnt += 1

        answer = max(answer, cnt)

        for letter in list(combi):
            teach_letter[ord(letter)] = False
    print(answer)
