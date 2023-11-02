import sys
from collections import deque
input = sys.stdin.readline


def is_not_deque_empty():
    if len(que) <= 0:
        print(-1)
        return False
    return True


if __name__ == "__main__":
    que = deque()
    for _ in range(int(input().strip())):
        command = input().strip()
        v = 0
        if len(command) > 4 and command[4] == "_":
            c, v = command.split()
            command = c
            v = int(v)
        if command == "push_front":
            que.extendleft([v])
        elif command == "push_back":
            que.append(v)
        elif command == "pop_front":
            if is_not_deque_empty():
                print(que.popleft())
        elif command == "pop_back":
            if is_not_deque_empty():
                print(que.pop())
        elif command == "size":
            print(len(que))
        elif command == "empty":
            print(int(len(que) == 0))
        elif command == "front":
            if is_not_deque_empty():
                print(que[0])
        elif command == "back":
            if is_not_deque_empty():
                print(que[-1])
