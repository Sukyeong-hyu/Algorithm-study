w, h, b = input().split()
w, h, b = int(w), int(h), int(b)

memory = w * h * b / 8 / 1024 / 1024

print(format(memory, '.2f'), 'MB')
