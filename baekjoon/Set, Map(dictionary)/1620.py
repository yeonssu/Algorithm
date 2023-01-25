import sys
N, M = map(int,sys.stdin.readline().rstrip().split())

pokemon_num = dict()
pokemon_str = dict()

for n in range(1,N+1):
    i = sys.stdin.readline().rstrip()
    pokemon_num[n] = i
    pokemon_str[i] = n

for m in range(M):
    Q = sys.stdin.readline().rstrip()
    if Q.isdecimal():
        print(pokemon_num.get(int(Q)))
    else:
        print(pokemon_str.get(Q))