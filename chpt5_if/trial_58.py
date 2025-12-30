# Hello User
usernames = ['admin','john','david','michael','mary']
if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username.title()}, would you like to see status report?")
        else:
            print(f"Hello {username.title()}, thank you for login in.")
else:
    print("We need to find more users.")