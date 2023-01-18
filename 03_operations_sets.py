set_a = {'Colombia', 'Mexico', 'Bolivia'}
set_b = {'Peru', 'Bolivia'}

## union
set_c = set_a.union(set_b)
print(set_c)

# it also can be done with | operator
set_c = set_a | set_b
print(set_c)

## intersection
set_c = set_a.intersection(set_b)
print(set_c)

# it also can be done with & operator
set_c = set_a & set_b
print(set_c)

## difference. returns a set with the values in a that are not in b
set_c = set_a.difference(set_b)
print(set_c)

# it also can be done with - operator
set_c = set_a - set_b
print(set_c)

## symetric difference. returns a set with all the values in both sets, excluding the values that are common for both
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# it also can be done with ^ operator
set_c = set_a ^ set_b
print(set_c)
