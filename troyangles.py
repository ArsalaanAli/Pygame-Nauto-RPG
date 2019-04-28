graph = []
x = int(input())
count = [[0 for i in range(x)] for i in range(x)]
for i in range(x):
    graph.append(input())
tot = 0
for i in range(x):
    if graph[x-1][i] == '#':
        count[x-1][i] = 1
        tot+=1
for y in range(x-2, -1, -1):
    for z in range(x):
        if graph[y][z] == '#':
            if z>0 and z<x-1:
                #IF DP
                count[y][z] = min(count[y+1][z], count[y+1][z+1], count[y+1][z-1])+1
            else:
                count[y][z] = 1
            tot += count[y][z]
print(tot)
