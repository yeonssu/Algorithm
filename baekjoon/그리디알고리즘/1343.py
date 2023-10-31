import sys
input = sys.stdin.readline


if __name__ == '__main__':
    board = list(map(str, input().strip()))
    answer = ""
    link = 0
    for i in range(len(board)):
        word = board[i]
        if word == ".":
            answer += "."
            link = 0
            continue
        else:
            link += 1
            if link == 4:
                answer += "AAAA"
                link = 0
            elif link == 2 and (i + 1 == len(board) or board[i + 1] == "."):
                answer += "BB"
                link = 0
            elif link == 3 and (i + 1 == len(board) or board[i + 1] == "."):
                print(-1)
                exit()
            elif link == 1 and (i + 1 == len(board) or board[i + 1] == "."):
                print(-1)
                exit()

    print(answer)
