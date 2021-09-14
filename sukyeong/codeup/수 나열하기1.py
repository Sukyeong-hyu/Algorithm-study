start, distance, result = input().split()
start, distance, result = int(start), int(distance), int(result)

for i in range(1, result):
    start += distance

print(start)