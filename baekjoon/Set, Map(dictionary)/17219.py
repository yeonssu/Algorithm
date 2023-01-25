import sys
N, M = map(int,input().split())

site_pw = dict()
for n in range(N):
    site, pw = sys.stdin.readline().strip().split()
    site_pw[site] = pw

for m in range(M):
    search = sys.stdin.readline().strip()
    print(site_pw[search])