"""classes for user and admin operations"""
class User:
    """User info class"""
    def __init__(self, f_name, l_name, email, age, address):
        """Initialize first and last name attributes."""
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.age = age
        self.address = address
        self.user_info = [f_name, l_name, email, age, address]
        self.login_attempts = 0
        
    def describe_user(self):
        """Display a summary of the user."""
        print("USER PROFILE:")
        for info in self.user_info:
            print(f"-{info if "@" in str(info) or isinstance(info, int) else info.title()}")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!\n")
    
    def show_login_attempts(self):
        """Shows the number of times user has logged in"""
        print(f"Login attempts: {self.login_attempts}")
        
    def increment_login_attempts(self):
        """Increases login attempts by 1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, f_name, l_name, email, age, address):
        super().__init__(f_name, l_name, email, age, address)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}. You're an Admin!\n")    
    
    def show_privileges(self):
        """Shows admin priviliges"""
        print('Admin Privileges are:')
        for i, privilege in enumerate(self.privileges, start=1):
            print(f"{i}. {privilege.capitalize()}")
