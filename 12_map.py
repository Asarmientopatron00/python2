numbers = [1, 2, 3, 4]
numbers_2 = list(map(lambda x: x*2, numbers))
print(numbers_2)

list_1 = [4, 6, 2, 3]
list_2 = [3, 9, 11] 
res = list(map(lambda x, y: x+y, list_1, list_2)) # if iterables sizes are not equal, the new list will have a length equals to the min size
print(res)

purchase = [
    {
        'id': 1,
        'product': 'Shirt',
        'price': 200
    },
    {
        'id': 2,
        'product': 'Jean',
        'price': 400
    },
    {
        'id': 4,
        'product': 'Gloves',
        'price': 50
    },
    {
        'id': 8,
        'product': 'Shoes',
        'price': 640
    },
]

def add_tax(item):
    item['tax'] = item['price']*0.25
    return item

prices = list(map(lambda x: x['price'], purchase))
newList = list(map(add_tax, purchase))
print(prices)
print(newList)