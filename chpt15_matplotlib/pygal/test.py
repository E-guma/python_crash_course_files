from itertools import combinations_with_replacement, count, islice, product
from math import prod
nums = [6,6,6]

products = []
die_sides = [10,6]
for n3 in range(1, nums[0]+1):
    for n2 in range(1, nums[0]+1):
        for n1 in range(1, nums[1]+1):
            result = n1 * n2 * n3
            if result not in products:
                products.append(result)
products.sort()
# print(products)
lst = [range(1,sides+1) for sides in die_sides]
cart_prod = list(product(item for item in lst))
print(list(item for item in lst))
# print(cart_prod)
# outcomes = 
# for i, outcome in zip(count(1), outcomes):
#     print() if i % 6 == 0 else print(outcome, end=' ')
   

