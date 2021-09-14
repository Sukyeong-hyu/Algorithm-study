letter = input()
if letter == 'q':
    print(letter)
else:
    while letter != 'q':
        print(letter)
        letter = input()
        if letter == 'q':
            print(letter)
            break