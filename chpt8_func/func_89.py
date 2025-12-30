def show_magicians(names):
    for name in names:
        print(name.title())



def make_great(names):
    for i,name in enumerate(names):
        names[i] = f'The Great {name}'
    return names