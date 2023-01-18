def inc(x):
    return x+1

def hof(x, func):
    return x+func(x)

inc2 = lambda x: x+2

res = hof(7, inc)
res_2 = hof(9, inc2)
res_3 = hof(15, lambda x: x**2)
print(res, res_2, res_3)