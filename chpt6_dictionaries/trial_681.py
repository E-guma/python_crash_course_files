pet_names = ['buddy', 'max', 'bella']
animal_kinds = ['dog', 'cat', 'rabbit']
owners = ['alice', 'bob', 'carol']

pets = []
for i in range(len(pet_names)):
    pet = {
        'pet_name': pet_names[i],
        'animal_kind': animal_kinds[i],
        'owner': owners[i]
    }
    pets.append(pet)
