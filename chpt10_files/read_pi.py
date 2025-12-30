# Read text file
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() 

pi = "".join(map(str.strip, lines))
print(pi[:52] + "...")   
print(len(pi))

print(pi.find('210507'))
print(pi[375818:375824])