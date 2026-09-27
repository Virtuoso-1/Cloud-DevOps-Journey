#All about Dictionaries 
#TRY 6.1 to 6.3 
person_info = {
        'first_name': 'Olamide',
        'last_name' : 'Olubode',
        'age': 22 ,
        'city' : 'Ibadan'

}

print(person_info['first_name'])
print(person_info['last_name'])
print(person_info['age'])
print(f"person_info['city']\n")

#Favorite Number 
fav_number = {
        'olamide': 6,
        'john' : 8,
        'james': 10,
        'favor' : 12
}

print(f"Olamide favorite number is {fav_number['olamide']}")
print(f"Favor favorite number is {fav_number['favor']}\n")


#glossary 
python_words = {
        'for loop' : 'To loop over the list of items',
        'if loop' : 'To continue running a code until the conditional statement is false',
        'conditional statement' : 'To check for the validity of statement'
}

print(f"for loop: {python_words['for loop']}")
print(f"if loop: {python_words['if loop']}")
print(f"conditonal staement: {python_words['conditional statement']}\n")

#Try  it yourself - 6.4 to 6.6
#6.4 - Glossary 2
for key, value in python_words.items():
    print(f"{key}:{value}")

#6.5 - Rivers 
rivers = {
    'nile' : 'egypt',
    'benue': 'nigeria',
    'suez canal': 'iran'
}

for key, value in rivers.items():
    print(f"The {key} runs through {value}")

for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)

print("\n")

#6.6 - Polling
people = ['sade', 'moyo', 'grace', 'peace', 'faith', 'simi']
languages = {
        'ayo': 'css', 
        'sade': 'c',
        'grace': 'python',
        'peace': 'python',
        'moyo': 'c#',
        'mujeeb': 'rust'
}

for name in people:
    if name in languages.keys():
        print(f"Thank you for responding {name}")
    else:
        print(f"{name},kindly take the poll for your favorite language.Thanks\n")


#Try it yourself
#6.7 - People
person_1 = {
        'first_name': 'Seun',
        'last_name' : 'Stephen',
        'age': 25 ,
        'city' : 'osun'

}

person_2 = {
        'first_name': 'Olamide',
        'last_name' : 'Olubode',
        'age': 22 ,
        'city' : 'Ibadan'

}

person_3 = {
        'first_name': 'rachel',
        'last_name' : 'akande',
        'age': 28 ,
        'city' : 'ekiti'

}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")


#6.9 - Favorite Places 

fav_places = {
        'isaac' : 'lagos',
        'dumola': 'ede',
        'olamide': 'ibadan'
}

for key, value in fav_places.items():
    print(f"{key}'s favorite is {value}")
print("\n")

#Favorite Number 2
fav_number2 = {
        'olamide': [6, 4, 2],
        'john' : [1, 3, 5, 7],
        'james': [10, 20, 30, 40],
        'favor' : [5, 10, 15]
}

for key, value in fav_number2.items():
    print(f"{key}'s favorite numbers are: {value}")


#Cities - 
cities = {
        'ibadan':{
                'language': 'yoruba',
                'size': '10000sq/km',
                'food': 'amala',
                'pop': 20000
                
        },

        'ife' : {
                'language': 'yoruba',
                'size': '100sq/km',
                'food': 'fufu',
                'pop': 10000
        },

        'ekiti' : {
                'language': 'ekate',
                'size': '3000sq/km',
                'food': 'ikokore',
                'pop': 5000
        }

}

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tpopulation: {city_info['pop']}")
    print(f"\tfood: {city_info['food']}")

print("\n")

#6.12 - Extension


        
    
