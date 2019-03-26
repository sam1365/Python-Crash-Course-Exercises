# exercise 3-1:
print("exercise 3-1:\n")

friends_names = ['russel', 'maisie', 'brad', 'kit']

print(friends_names[0].title())
print(friends_names[1].title())
print(friends_names[2].title())
print(friends_names[3].title())

# exercise 3-2:
print("exercise 3-2:\n")

print("Hi " + friends_names[0].title() + " how are you?")
print("Hi " + friends_names[1].title() + " how are you?")
print("Hi " + friends_names[2].title() + " how are you?")
print("Hi " + friends_names[3].title() + " how are you?")

# exercise 3-4:
print("exercise 3-4:\n")

guests = ['russel crowe', 'maisie williams', 'brad pitt', 'kit harington' , 'sophie turner']

print("Dear " + guests[0].title() + " join us for dinner party")
print("Dear " + guests[1].title() + " join us for dinner party")
print("Dear " + guests[2].title() + " join us for dinner party")
print("Dear " + guests[3].title() + " join us for dinner party")
print("Dear " + guests[4].title() + " join us for dinner party")

# exercise 3-5:
print("exercise 3-5:\n")

print("Sorry about this, but our dear guest " + guests[0].title() + "can't come for dinner!")
del guests[0]
guests.append('michael haneke')
print("Dear " + guests[0].title() + " join us for dinner party")
print("Dear " + guests[1].title() + " join us for dinner party")
print("Dear " + guests[2].title() + " join us for dinner party")
print("Dear " + guests[3].title() + " join us for dinner party")
print("Dear " + guests[4].title() + " join us for dinner party")

# exercise 3-6:
print("exercise 3-6:\n")

print("We got a bigger table!\n")

guests.insert(0, 'keira knightley')
guests.insert(4, 'johnny depp')
guests.append('nicole kidman')

print("Dear " + guests[0].title() + " join us for dinner party")
print("Dear " + guests[1].title() + " join us for dinner party")
print("Dear " + guests[2].title() + " join us for dinner party")
print("Dear " + guests[3].title() + " join us for dinner party")
print("Dear " + guests[4].title() + " join us for dinner party")
print("Dear " + guests[5].title() + " join us for dinner party")
print("Dear " + guests[6].title() + " join us for dinner party")
print("Dear " + guests[7].title() + " join us for dinner party")

# exercise 3-7:
print("exercise 3-7:\n")
print("Sorry about this, but our table didn't arrive on time, we have room just for two! ")

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

dear_guest = guests.pop(2)
print("Sorry dear " + dear_guest.title() + " we don't have enough table!") 

print("Dear " + guests[0].title() + " join us for dinner party")
print("Dear " + guests[1].title() + " join us for dinner party")

del guests[0]
del guests[0]
print(guests)

# exercise 3-8:
print("exercise 3-8:\n")

visit_places = ['rome', 'paris', 'venice', 'london', 'dresden', 'spain', 'rio de janeiro']
print(visit_places)
print(sorted(visit_places))
print(visit_places)
print(sorted(visit_places, reverse=True))
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.sort()
print(visit_places)
visit_places.sort(reverse=True)
print(visit_places)

# exercise 3-9:
print("exercise 3-8:\n")
guests = ['russel crowe', 'maisie williams', 'brad pitt', 'kit harington' , 'sophie turner']
print("The number of our guests for dinner is: " + str(len(guests)))

# exercise 3-10:
print("exercise 3-10:\n")
mountains = ['everest', 'k2', 'makalu', 'shishapanga', 'Kangchenjunga', 'Lhotse']

print("Original Order:")
print(mountains)
print("Sorted:")
print(sorted(mountains))

print("Original Order:")
print(mountains)
print("Reverse Sorted:")
print(sorted(mountains, reverse=True))

print("Original Order:")
print(mountains)

print("Reversed:")
mountains.reverse()
print(mountains)

print("Original Order:")
mountains.reverse()
print(mountains)

print("Sort Alphebetical: ")
mountains.sort()
print(mountains)

print("Sort Reverse Alphebetical: ")
mountains.sort(reverse = True)
print(mountains)

