h, w = input().split()
h, w = int(h), int(w)
n = int(input())  # 놓을 수 있는 막대의 개수


play = []  # 놀이판 좌표

# 좌표 만들기
for i in range(h+1):
    play.append([])
    for j in range(w+1):
        play[i].append(0)

# 막대의 개수에 맞게 막대 길이(l), 방향(d), 좌표(x, y) 입력 받기
for i in range(n):
    l, d, x, y = input().split()
    l, d, x, y = int(l), int(d), int(x), int(y)
    if d == 0:
        for j in range(l):
            play[x][y+j] = 1
    else:
        for j in range(l):
            play[x+j][y] = 1


# 좌표 출력하기
for i in range(1, h+1):
  for j in range(1, w+1):
    print(play[i][j], end=' ')
  print()