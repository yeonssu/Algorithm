x,y,w,h = map(int,input().split())

array = [[0]*w for i in range(h)]
array[y-1][x-1] = 1


left = x
right = w-x
top = y
bottom = h-y

# if left==0 : left=1
# if right==0 : right=1
# if top==0 : top=1
# if bottom==0 : bottom =1

print(min(left,right,top,bottom))