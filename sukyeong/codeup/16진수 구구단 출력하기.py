# A~F 중 한 숫자 입력받기
num = input()
num = int(num, 16)

for i in range(1, 16):
    print('%X' % num, '*%X' % i, '=%X' % (num * i), sep='')