V, E = 5,6
edges = [(1,2), (2,3), (1,4), (2,4),(1,5),(3,5)]

# make Adjacent Matrix
AM = [[0]*(V+1) for i in range(V+1)]

for s,e in edges:
    AM[s][e] = 1

for x in AM:
    print(x)

# make Adjacent List
AL = [[] for i in range(V+1)]

for s,e in edges:
    AL[s].append(e)

for x in AL:
    print(x)
