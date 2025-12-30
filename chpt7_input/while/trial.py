# Pizza Topping Order System
toppings = [] # list to store pizza toppings

# prompt for user input
prompt = "Please enter your pizza toppings:"
prompt += "\nEnter 'done' to finish your order:\n"

# program logic
while True:     # accept toppings until user is done
    topping = input(prompt) # get user input
    
    if topping.lower() == 'done':   # check if user is done
        print('Here\'s your order:')
        for order in toppings:
            print(f"\t{order.title()}")
        
        proceed = ""
        # confirm order or cancel
        while True:  # return here if input is invalid 
            proceed = input("\nType 'OK' to continue OR 'CANCEL'\n")
            if proceed.lower() not in ['ok','cancel']:  # check valid input
                print("OOPS! Type in the right keywords")
                continue
            else:
                break
        
        if proceed.lower() == 'ok':  # proceed with order
            print("Your order will soon be ready.")
        
        elif proceed.lower() == 'cancel':   # cancel order
            print('Your order has been cancelled\nLets go again\n')
            while toppings:
                toppings.pop()
            continue
        
        break
    
    else:
        toppings.append(topping)    # add topping to list
        print(f"{topping.title()} added.\n")