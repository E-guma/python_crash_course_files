first_names = ['rhoda', 'oliver', 'victor']
last_names = ['james', 'davis', 'garcia']
ages = ['30', '25', '21']
cities = ['new york', 'los angeles', 'chicago']

people = []

for i in range(len(first_names)):
    people.append({
        'first_name': first_names[i],
        'last_name': last_names[i],
        'age': ages[i],
        'city': cities[i]
    })
    
for i, person in enumerate(people, start=1):
    print(f"\nPerson Details {i}:")
    for k, v in person.items():
        print(f"{k.title()}: {v.title()}")