import json

filename = 'fav_num.json'
        
def get_user_info(file):
    """Get user info and save it to a file."""
    user = {
        'username': input("Enter your name: "),
        'fav_num': input("What's your favorite number: ")        
    }
    with open(file, 'w') as f:
        json.dump(user, f)
    return user

def get_saved_user_info(file):
    """Returns saved user info from file if file exists"""
    try:
        with open(file) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    
def check_user(user):
    """Checks to see if current user is previous user"""
    print(f"Previous Login: {user['username']}")
    confirm_user = input("Is this You Y/N: ")
    return confirm_user.lower() == 'y'
                
def welcome_user():
    user = get_saved_user_info(filename)
    if user:
        if check_user(user):
            print(f"WELCOME BACK {user['username']}!")
            print(f"I know your favorite number is {user['fav_num']}.")
        else:
            # The previous user was not confirmed, so get new info
            new_user = get_user_info(filename)
            print(f"Welcome {new_user['username']}. We'll remember you next time")
            
    else:
        # No saved info found
        new_user = get_user_info(filename)
        print(f"Welcome {new_user['username']}. We'll remember you next time")
    
welcome_user()    
