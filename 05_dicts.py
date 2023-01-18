import random

dict = {}
for i in range(1, 11):
    dict[i] = i*2

print(dict)

dict_2 = {i: i*2 for i in range(1, 11)}
print(dict_2)

countries = ['Colombia', 'Argentina', 'Mexico']
population = {}
for country in countries:
    population[country] = random.randint(1, 2000)
print(population)

population_2 = {country: random.randint(1, 2000) for country in countries}
print(population_2)

names = ['Andres', 'Valeria', 'Leia', 'Wanda']
ages = [24, 28, 6, 3]

info = {name: age for (name, age) in list(zip(names, ages))}
print(info)

result = {country: pop for (country, pop) in population_2.items() if pop > 1000}
print(result)

text = 'Hello, my name is Andres'
unique_vowels = {v: v.upper() for v in text.lower() if v in 'aeiou'}
print(unique_vowels)