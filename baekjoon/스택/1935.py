import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    word = input().strip()
    dic = dict()
    for i in range(n):
        dic[i] = int(input().strip())

    stack = []
    for w in word:
        if 'A' <= w <= 'Z':
            stack.append(dic.get(ord(w) - ord('A')))
        else:
            symbol2 = stack.pop()
            symbol1 = stack.pop()

            if w == '+':
                stack.append(symbol1 + symbol2)
            elif w == '-':
                stack.append(symbol1 - symbol2)
            elif w == '*':
                stack.append(symbol1 * symbol2)
            elif w == '/':
                stack.append(symbol1 / symbol2)
    print('%.2f' % stack[0])
