num = int(input())  # 번호를 부른 횟수
a = list(map(int, input().split()))

for i in range(num):
    a[i] = int(a[i])

print(min(a))

