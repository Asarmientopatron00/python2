def get_population():
    keys = ['Colombia', 'Argentina']
    values = [100, 200]
    return keys, values

def population_by_country(data, country):
    return list(map(lambda x: x['population'], filter(lambda x: x['country'] == country, data)))