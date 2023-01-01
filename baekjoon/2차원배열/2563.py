entire_area = [[0]*100 for i in range(100)]
paper_width = []
paper_height = []

n = int(input())

for i in range(n):
    w, h = map(int, input().split())
    paper_width.append(w) 
    paper_height.append(h)

for i in range(n):
    for j in range(10):
        for k in range(10):
            entire_area[paper_width[i]+j][paper_height[i]+k] = 1

cnt = 0
for i in range(100):
    cnt += entire_area[i].count(1) 

print(cnt) 