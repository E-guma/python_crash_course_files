# alien_color-point allocation
alien_color = 'red'
if alien_color == "green":
    point = 5
elif alien_color == "yellow":
    point = 10
else:
    point = 15
print(f"You earned {point} points.")

# life stages
age = 66
if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "elder"
if stage == "adult" or stage == "elder": # Different article for adult & elder
    article = "an" 
else:
    article = "a"
print(f"You are {article} {stage}.")