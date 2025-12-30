while True:
    print("Enter 'CANCEL' to end Poll.")
    response = input("Tell us why you like programming: ")
    if response.lower() == 'cancel':
        break
    else:
        with open('programming_poll.txt', 'a') as file_object:
            file_object.write(response.capitalize() +'\n')