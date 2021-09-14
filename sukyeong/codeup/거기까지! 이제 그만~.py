num = int(input())
count = 0
total = 0

while total < num:
    count += 1
    total += count
    if total >= num:
        print(total)
        break