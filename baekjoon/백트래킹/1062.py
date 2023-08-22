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
    for combi in combinations(alphabet, K - 5):
        cnt = 0
        teach_letter = list(combi)
        teach_letter.extend(["a", "n", "t", "i", "c"])
        print(teach_letter)
        for word in words:
            for i in range(len(word)):
                if word[i] in teach_letter:
                    if i == len(word) - 1:
                        cnt += 1
                else:
                    break
        answer = max(answer, cnt)
    print(answer)
