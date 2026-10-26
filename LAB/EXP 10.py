g = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)], 3: []}
h = {0: 4, 1: 3, 2: 1, 3: 0}
open_list = [(h[0], 0)]
cost = {0: 0}

while open_list:
    open_list.sort()
    _, n = open_list.pop(0)

    if n == 3:
        print("Goal reached:", cost[n])
        break

    for v, w in g[n]:
        new = cost[n] + w
        if v not in cost or new < cost[v]:
            cost[v] = new
            open_list.append((new + h[v], v))
