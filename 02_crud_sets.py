set_countries = {'Colombia', 'Mexico', 'Bolivia'}

# size
size = len(set_countries)

# in
col = 'Colombia' in set_countries

# add
set_countries.add('Peru')

#  update
set_countries.update({'Argentina', 'Ecuador'})

# remove
set_countries.remove('Bolivia')

# remove if exists
set_countries.discard('Bolivia')

# clear
set_countries.clear()
