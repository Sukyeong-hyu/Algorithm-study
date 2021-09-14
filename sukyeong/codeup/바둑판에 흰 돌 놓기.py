play = []
count = int(input())
num = 0

for i in range(20):
    play.append([])
    for j in range(20):
        play[i].append(0)

while num != count:
    x, y = input().split()
    x, y = int(x), int(y)
    play[x][y] = 1
    num += 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(play[i][j], end=' ')
  print()