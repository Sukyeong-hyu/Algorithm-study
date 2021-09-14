n = int(input())  # 출석 번호 부르는 횟수
a = input().split()

# 리스트 a 안에 있는 숫자들 정수로 변환
for i in range(n):
    a[i] = int(a[i])

# 출석부 리스트 만들기
name = []
for i in range(24):
    name.append(0)

# 부르는 인덱스 숫자 올리기
for i in range(n):
    name[a[i]] += 1

# 출석부 출력하기
for i in range(1, 24):
    print(name[i], end=' ')