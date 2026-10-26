b = [' '] * 9

def show():
    print(b[0:3])
    print(b[3:6])
    print(b[6:9])

for i in range(9):
    show()
    p = int(input("Enter position (0-8): "))
    if b[p] == ' ':
        b[p] = 'X' if i % 2 == 0 else 'O'
    else:
        print("Position occupied")
        continue

show()
