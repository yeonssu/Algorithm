import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    num = list(map(str, input().strip()))
    stack = []
    for n in num:
        # n : 다음 수 / stack[-1] : 이전 수 / -> 이전 수가 더 큰 경우 스택을 제외, 자신을 추가
        while stack and n > stack[-1] and K > 0:
            stack.pop()
            K -= 1
        stack.append(n)
    if K > 0:
        print(''.join(stack[:-K]))
    else:
        print(''.join(stack))
