start, multiply, distance, result = input().split()
start, multiply, distance, result = int(start), int(multiply), int(distance), int(result)

for i in range(1, result):
    start *= multiply
    start += distance

print(start)