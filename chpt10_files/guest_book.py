while True:
    name = input("Please enter your name\nType 'end' to end programme: ")
    if name.lower() == 'end':
        print('Programme has ended')
        break
    else:
        print(f'Hello {name.title()}, WELCOME!\n')
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f'{name.title()} just visited guest_book.py.\n')