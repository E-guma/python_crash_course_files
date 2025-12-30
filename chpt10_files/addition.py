while True:
    print("Add two numbers\n".upper())
    try:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
    except ValueError:
        print("Please Enter a number only!")
        continue
    else:
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
        break
    
    