maze = []

for i in range(11):
    maze.append([])
    for j in range(11):
        maze[i].append(0)

for i in range(1, 11):
    a = input().split()
    for j in range(1, 11):
        maze[i][j] = int(a[j-1])



for i in range(1, 11):
    for j in range(1, 11):
        print(maze[i][j], end=' ')
    print()


