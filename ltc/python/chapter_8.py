#Functions
#Try it yourself 8.1 & 8.2
def display_message():
    #Print information about this chapter learnings
    print("I'm currently learning how to use functions")

display_message()

#Favorite book
def favorite_book(title):
    #Print the favorite book 
    print(f"One of my favorite books is {title}\n")

favorite_book('The 5AM Club')

#Positonal & keywords arguments and defualt value - Try it yourself 8.3 to 8.5
#T Shirt
def make_shirt(size, message):
    #A function that accept size and the message to be printed on the shirt
    print(f"The shirt size is {size}.")
    print(f"{message}\n")

make_shirt('XL', "Don't just die. Time is your ally.")

#Large shirt - 8.4 - Modifying the makeshirt function
#Making use of default value 
def make_shirt(message, size='large'):
    #A function that accept size and the message to be printed on the shirt
    print(f"The shirt size is {size}.")
    print(f"{message}\n")

make_shirt("You will and you can!")

#8.5 - Cities 
def describe_city(city, country= 'Rome'):
    #A function that print a simple sentence using the argument passed
    print(f"{city} is in {country}\n")

describe_city('Italy')
describe_city('Sicily')
describe_city('Como')


#Return Values, Optional Argument, Returning dictionaries - Try it yourself 8.6 to 8.8
#8.6 - City Names 
def city_country(city, country):
    #Return a the name of a city and its county in formatted string
    formatted = f"{city}, {country}"
    return formatted.title()

city1 = city_country('italy', 'rome')
print(city1)
city2 = city_country('london', 'uk')
print(city2)


#8.7 - Album 
def make_album(artist_name, album_title, no_of_songs=None):
    #A function that builds a dictionary describing a music album
    album = {'name': artist_name, 'title':album_title}
    if no_of_songs:
        album['songs'] = no_of_songs
    return album

album_1 = make_album('Asake', 'Work of Art')
album_2 = make_album('Seyi Vibez', 'Swaggu')
album_3 = make_album('Olamide', 'YBNL')

print(album_1)
print(album_2)
print(f"{album_3}\n")

album_4 = make_album('Femilevite', 'Afrojelenke', no_of_songs=11)
print(album_4)


#8.8 User Albums - Starting with the existing function: make_album 

def make_album(artist_name, album_title, no_of_songs=None):
    #A function that builds a dictionary describing a music album
    album = {'name': artist_name, 'title':album_title}
    if no_of_songs:
        album['songs'] = no_of_songs
    return album

while True:
    print("Please enter album's title and artist")
    print("Enter 'q' to quit at ant time")
    title = input("Enter the album's title")
    if title == 'q':
        break

    artist = input("Enter the name of the artist")
    if artist == 'q':
        break


    album = make_album(artist, title)
    print(f"{album}\n")



