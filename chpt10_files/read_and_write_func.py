"""A module to read and write files

This module contains a class with two functions:
- ReadWrite: A class to read and write files
- create_file: A function to create a file with given names
- read_file: A function to read the contents of a file"""

class ReadWrite:
    """A class to read and write files"""
    
    def __init__(self, filename):
        self.filename = filename

    def create_file(self, *names):
        """Creates a file with the given file name and adds some text"""
        with open(self.filename, 'w') as file_object:
            for name in names:
                file_object.write(name.title() + "\n")
        print(f'File {filename} created')
        
    def read_file(self):
        """Returns the contents of a file"""
        with open(self.filename) as file_object:
            contents = file_object.read()
            return contents.rstrip()
                
#create_file('cats.txt','mice', 'kitty', 'pussy')
#create_file('dogs.txt', 'bingo', 'roger', 'bull')