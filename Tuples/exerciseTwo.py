from exerciseOne import marvel_characters

print(marvel_characters)


superman,batman,wonder_woman,shazzam,black_adam,captain,iron_man,thor,hulk,vision,*villains = marvel_characters

print(superman)
print(batman)
print(wonder_woman)
print(shazzam)
print(black_adam)
print(captain)
print(iron_man)
print(thor)
print(hulk)
print(vision)
print(*villains)



#  Q-2

fruits = ('apple', 'orange')
veggies = ('Tomato', 'Onion')
dairy  = ('eggs', 'meat')
food_stuff_tp  = fruits + veggies + dairy
print(food_stuff_tp)

# Q-3

food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

# Q-4

print(food_stuff_tp[2:4])

# Q-5
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])

# Q-6

food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)
del food_stuff_tp
# print(food_stuff_tp)

# Q-7

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
