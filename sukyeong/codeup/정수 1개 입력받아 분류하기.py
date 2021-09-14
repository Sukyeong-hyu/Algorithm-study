num = int(input())

if num % 2 == 0:
    if num < 0:
       print("A")
    else:
        print("C")
elif num > 0:
    print("D")
else:
    print("B")