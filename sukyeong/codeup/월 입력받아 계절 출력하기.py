month = int(input())

if month == 12 or month < 3:
    print('winter')
elif month < 6:
    print('spring')
elif month < 9:
    print('summer')
else:
    print('fall')