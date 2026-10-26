rooms = {'A': 1, 'B': 0}
pos = 'A'

for room in rooms:
    pos = room
    if rooms[pos] == 1:
        print(pos, "is Dirty - Cleaning")
        rooms[pos] = 0
    else:
        print(pos, "is Clean")

print("Final Status:", rooms)
