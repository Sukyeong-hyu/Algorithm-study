play = []  # 바둑판

# 바둑판 좌표 만들기
for i in range(20):
    play.append([])
    for j in range(20):
        play[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        play[i+1][j+1] = int(a[j])

# 결과 바둑판 출력하기
for i in range(1, 20):
    for j in range(1, 20):
        print(play[i][j], end=' ')
    print()
