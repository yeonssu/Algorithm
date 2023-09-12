import sys
from functools import cmp_to_key

input = sys.stdin.readline


def separate(word):
    words = []
    sub = ""
    for i in range(len(word)):
        if word[i].isdigit():
            sub += word[i]
        else:
            if len(sub) != 0:
                words.append(sub)
                sub = ""
            words.append(word[i])
    if len(sub) != 0:
        words.append(sub)

    return words


def compare(file1, file2):
    idx = min(len(file1), len(file2))
    for i in range(idx):
        # 같으면 건너 뛰기
        if file1[i] == file2[i]:
            continue
        # 하나가 숫자면 숫자인 게 우선
        if file1[i].isdigit() and not file2[i].isdigit():
            return -1
        elif not file1[i].isdigit() and file2[i].isdigit():
            return 1
        # 둘 다 숫자면 숫자가 작은 것이 우선
        elif file1[i].isdigit() and file2[i].isdigit():
            # 같은 값을 가지는 숫자일 경우, 앞에 붙은 0의 개수가 적은 것이 앞에 온다.
            if int(file1[i]) == int(file2[i]):
                cnt1 = len(file1[i]) - len(file1[i].lstrip('0'))
                cnt2 = len(file2[i]) - len(file2[i].lstrip('0'))
                return cnt1 - cnt2
            else:
                return int(file1[i]) - int(file2[i])


        # 둘 다 문자면, AaBbCc...XxYyZz의 순서
        elif not file1[i].isdigit() and not file2[i].isdigit():
            if file1[i].lower() == file2[i].lower():
                return file1[i] - file2[i]
            else:
                return file1[i].lower() - file2[i].lower()

    return len(file1) - len(file2)


if __name__ == "__main__":
    N = int(input().strip())
    explorer = []
    for _ in range(N):
        words = separate(input().strip())
        explorer.append(words)

    explorer.sort(key=cmp_to_key(compare))
    for file in explorer:
        answer = ""
        for f in file:
            answer += str(f)
        print(answer)
