from read_and_write_func import ReadWrite as rw

filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
    
with open('Moby_Dick.txt', encoding='utf-8', errors='ignore') as md:
    contents = md.read()
    print(contents.lower().count('the'))
    
    

