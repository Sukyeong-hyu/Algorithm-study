n = int(input())  # 출석 번호 부르는 횟수
a = list(map(int, input().split()))
reverse_a = []

# 리스트 a 안에 있는 숫자들 정수로 변환
for i in range(n):
    a[i] = int(a[i])

# 거꾸로 출력하기
for i in range(n-1, -1, -1) :
  print(a[i], end=' ')
