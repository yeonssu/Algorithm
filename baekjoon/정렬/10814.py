import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().strip())
    members = []
    for i in range(N):
        age, name = map(str, input().strip().split())
        members.append((int(age), name, i))
    members.sort(key=lambda x: (x[0], x[2]))
    for member in members:
        print(member[0], member[1])
