from collections import deque

g = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
q = deque([1])
visited = []

while q:
    n = q.popleft()
    if n not in visited:
        visited.append(n)
        q.extend(g[n])

print(visited)
