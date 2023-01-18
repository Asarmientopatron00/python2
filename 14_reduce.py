import functools

numbers = [10, 22, 334, 44]

result = functools.reduce(lambda res, item: res+item, numbers)
print(result)