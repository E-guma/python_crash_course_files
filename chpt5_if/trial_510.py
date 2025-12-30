# Checking Usernames (Case Insensitive)
current_users = ['mike','DaVe','victor','guma']
new_users = ['Mike','davE','anna','sara']
for name in new_users:
    if name.lower() in [user.lower() for user in current_users]:
        print('Username already taken. Please enter a new username.')
    else:
        print('Username is available.')

# Ordinal Numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(str(number)+suffix)