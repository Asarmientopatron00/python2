def increment():
    print(price)

def increment_2():
    price = 300 # local scope for this function
    print(price)

def increment_3():
    res = 100
    print(res)

price = 100 # global
## print(res) # we can not access to res in function increment_3. It is in a different scope
increment()