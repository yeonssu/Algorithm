def solution(rows, columns, queries):
    board = []
    for i in range(rows):
        sub = []
        for j in range(1, columns + 1):
            sub.append(i * columns + j)
        board.append(sub)

    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        start_point = board[x1][y1]
        circle = [board[x1][y1]]

        for k in range(x1, x2):
            board[k][y1] = board[k + 1][y1]
            circle.append(board[k][y1])

        for k in range(y1, y2):
            board[x2][k] = board[x2][k + 1]
            circle.append(board[x2][k])

        for k in range(x2, x1, -1):
            board[k][y2] = board[k - 1][y2]
            circle.append(board[k][y2])

        for k in range(y2, y1, -1):
            board[x1][k] = board[x1][k - 1]
            circle.append(board[x1][k])

        board[x1][y1 + 1] = start_point
        answer.append(min(circle))

    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
solution(100, 97, [[1, 1, 100, 97]])
