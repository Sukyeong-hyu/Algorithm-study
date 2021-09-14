num = int(input())
total = 0

for i in range(num+1):
    if i % 2 == 0:
        total = total + i
print(total)