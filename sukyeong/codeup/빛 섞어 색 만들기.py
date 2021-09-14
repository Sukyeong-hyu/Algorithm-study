r, g, b = input().split()
r, g, b = int(r), int(g), int(b)

for k in range(r):
    for i in range(g):
        for j in range(b):
            print(k, i, j)


print(r*g*b)