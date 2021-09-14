num1, num2, num3 = input().split()
num1, num2, num3 = int(num1), int(num2), int(num3)

result = 1

while result % num1 != 0 or result % num2 != 0 or result % num3 != 0:
    result += 1

print(result)
