#Creating the list of guest to be invited
guest_list = ['Isaac', 'Tunde', 'Ade']
print(f"You're welcome to the party,  {guest_list[0]}.")
print(f"Bring me the brightest flower, {guest_list[2]}.")

#Modifying the guest list
print(f"\n{guest_list[1]} won't be able to make it.")

guest_list[1] = 'Favour' 
print(f"\nYou're welcome to the party,  {guest_list[0]}.")
print(f"Bring me the brightest flower, {guest_list[2]}.")
print(f"Welcome to the club, {guest_list[1]}.")

#Adding more guest to the list

guest_list.insert(0, 'Steven')
guest_list.insert(2, 'Frances')
guest_list.append('olamide')

print(f"\nYou're cordially invited to the party, {guest_list[0]}.")
print(f"You're cordially invited to the party, {guest_list[1]}.")
print(f"You're cordially invited to the party, {guest_list[2]}.")
print(f"You're cordially invited to the party, {guest_list[3]}.")
print(f"You're cordially invited to the party, {guest_list[4]}.")
print(f"You're cordially invited to the party, {guest_list[5]}.")

#Shrinking the list

print("\nThe big table is no more available, I have space for only 3 people")

shrink1 = guest_list.pop()
print(f"\nI'm sorry the place can no longer contain us, {shrink1}")
shrink2 = guest_list.pop()
print(f"I'm sorry the place can no longer contain us, {shrink2}")
shrink3 = guest_list.pop()
print(f"I'm sorry the place can no longer contain us, {shrink3}")


print(f"\nYou're still cordially invited to the party, {guest_list[0]}.")
print(f"You're still cordially invited to the party, {guest_list[1]}.")
print(f"You're still cordially invited to the party, {guest_list[2]}.")


#List sorting exercises
countries = ['Berlin', 'Oslo', 'Germany', 'Italy', 'Japan', 'Argentina']
print(f"\n{countries}")
print(sorted(countries))
print(f"This is the original list created, {countries}")

#Printing the list in reverse order
countries.reverse()
print(countries)

#Changed back to the original order and then sorted
countries.reverse()
print(countries)
countries.sort()
print(countries)

#Sort the list in reverse order
countries.sort(reverse=True)
print(countries)

#Dealing with intentional error - index error
print(countries[6])


