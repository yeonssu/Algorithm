import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    s = deque(input().strip())
    word = ''
    while s:
        word += s.popleft()
        if word == 'pi' or word == 'ka' or word == 'chu':
            word = ''

    if word == '':
        print('YES')
    else:
        print('NO')
