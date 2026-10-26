from itertools import permutations

d = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
best = 999
path = None

for p in permutations([1, 2]):
    route = (0,) + p + (0,)
    cost = sum(d[route[i]][route[i+1]] for i in range(3))
    if cost < best:
        best, path = cost, route

print("Path:", path)
print("Cost:", best)
