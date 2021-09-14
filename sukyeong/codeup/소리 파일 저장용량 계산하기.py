h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)

memory = h * b * c * s / 8 / 1024 / 1024
print(round(memory, 1), 'MB')
