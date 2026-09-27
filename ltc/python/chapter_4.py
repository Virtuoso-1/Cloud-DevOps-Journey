#Looping over lists - TRY 4.1
pizzas = ['pepperoni', 'chicken', 'meat', 'turkey']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("I really love pizza\n")

#Looping over lists - TRY 4.2
animals = ['goat', 'dog', 'lion', 'tiger']
for animal in animals:
    print(animal)

#Modifying the list of animals
animals[0] = 'cat'
for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals have four legs.")


#Working with range and list comprehensions - TRY 4.3 to 4.9
for value in range(1,21):
    print(value)

one_million = [value for value in range(1,1000001)]
print(min(one_million))
print(max(one_million))
print(f"sum(one_million)\n")

odd_numbers = [value for value in range(1,20,2)]
for odd in odd_numbers:
    print(odd)
print("\n")

#Multiples of threes
threes = [value for value in range(3,30,3)]
for three in threes:
    print(three)
print("\n")

#Cubes of the first 10 number
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)
print("\n")

#Using the pizzas and animals list to practice list slicing -TRY 4.10 to 4.12
print(pizzas[:2])
print(animals[:3])
print(f"The last three animals are: {animals[-3:]}\n")

#Copying the contents of a list into another and adding more
friend_pizzas = pizzas[:]
friend_pizzas.append('hotdog')
pizzas.append('creamy')

print(f"This is the original list of pizza with appended values: {pizzas}")
print(f"This is my friend favorite pizzas: {friend_pizzas}\n")


#Working with Tuples 
buffet = ('rice','beans', 'plantain', 'fish', 'egg')
for buffet in buffet:
    print(buffet)
print(f"\n")

#Changing some values in the tuples by reassinging the variable
buffet = ('rice','potatoes', 'plantain', 'yam', 'egg')
for buffet in buffet:
    print(buffet)