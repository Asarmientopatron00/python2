def increment(x=1):
    return x+1

increment_lambda = lambda x : x + 1

full_name = lambda first_name, last_name: f'{first_name.title()} {last_name.title()}'

res = increment(10)
res_2 = increment_lambda(30)
res_3 = full_name('andres', 'sarmiento')

print(res, res_2, res_3)