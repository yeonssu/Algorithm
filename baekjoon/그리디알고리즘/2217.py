import sys
input = sys.stdin.readline

if __name__ == '__main__':
    loops = [int(input().strip()) for _ in range(int(input()))]
    loops.sort(reverse=True)
    answer = 0
    for i in range(len(loops)):
        answer = max(answer, loops[i] * (i + 1))
    print(answer)