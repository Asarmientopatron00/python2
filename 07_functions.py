def my_print(text):
    print(text)

def my_sum(a,b):
    return a+b

def find_volume(l=1, w=1, h=1): # default values with =
    return l*w*h

def sev_returns():
    return 'Hello', 66, True # we can return severeal values using commas

my_print('This is my print')
sum = my_sum(6, 88)
print(sum)

vol = find_volume(5, 4, 3)
vol_2 = find_volume() # if args are not passed, the functions uses default values
vol_3 = find_volume(h=5) # if not all args are passes, functions uses default values for the not passes values
print(vol, vol_2, vol_3)

string, num, boolean = sev_returns()
print(string, num, boolean)