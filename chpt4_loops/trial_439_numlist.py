"""for num in range(1,21):
    print (num)"""
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))
odd = list(range(1,20,2))
threes = list(range(3,31,3))
cubes = [num**3 for num in range(1,11)]
print(odd, threes, cubes)