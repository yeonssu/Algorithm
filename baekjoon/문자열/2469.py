import sys
input = sys.stdin.readline


def divide():
    front = []
    back = []
    for i in range(len(graph)):
        if graph[i][0] == "?":
            front = graph[:i]
            back = graph[i + 1:]
    return front, back


if __name__ == "__main__":
    k = int(input().strip())
    n = int(input().strip())
    end = list(map(str, input().strip()))
    start = sorted(end)
    graph = [list(map(str, input().strip())) for _ in range(n)]
    front, back = divide()
    for layer in front:
        for i in range(len(layer)):
            if layer[i] == "-":
                start[i + 1], start[i] = start[i], start[i + 1]

    for layer in reversed(back):
        for i in range(len(layer)):
            if layer[i] == "-":
                end[i + 1], end[i] = end[i], end[i + 1]

    answer = ["*"] * (k - 1)
    for i in range(k - 1):
        if start[i] == end[i]:
            continue
        else:
            answer[i] = "-"
            start[i + 1], start[i] = start[i], start[i + 1]

    for s, f in zip(start, end):
        if s != f:
            print("x" * (k - 1))
            exit()

    for a in answer:
        print(a, end="")
