A, B, V = map(int, input().split())

if((V-B)%(A-B)==0):
    day = (V-B)//(A-B)
else:
    day = (V-B)//(A-B) + 1

print(day)

# while(location<V):
#     location+=A
#     if(location>=V): 
#         print(day)
#         break
#     location-=B
#     if(location>=V):
#         print(day)
#         break
#     day+=1


    