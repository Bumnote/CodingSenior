from itertools import permutations

ex_list = [1, 2, 3]
for per_list in permutations(ex_list, 2):
    print(per_list)
