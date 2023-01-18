import utils

a, b = utils.get_population()
data = list(map(lambda x,y: {'country': x, 'population': y}, a, b))

def run():
	country = input('Type a country: ')
	population_of_country = utils.population_by_country(data, country)
	print(population_of_country)

# this sentence allows us to use this file as a module and an script without getting errors
# when I run this file, run() function will be called by default
if __name__ == '__main__':
	run()