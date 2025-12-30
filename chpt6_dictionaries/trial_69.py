favourite_places = {
    'john': ['paris', 'new york'],
    'dave':['rome','italy','las vegas'],
    'sarah':['cairo','giza'],
    }
for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"- {place.title()}")
    print("\t")