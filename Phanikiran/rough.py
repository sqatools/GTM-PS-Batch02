set1 = {4, 7, 9, 2, 'a', 'b'}
set2 = {4, 2, 'a', 11, 33, 55}

results = set1.difference(set2)
print(results)

set1.difference_update(set2)
print(set1)