g = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
visited = []

def dfs(n):
    if n not in visited:
        visited.append(n)
        for x in g[n]:
            dfs(x)

dfs(1)
print(visited)
