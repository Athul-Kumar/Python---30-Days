
# Q-1 creating empty tuple

empty_tuple = ()

# second method

empty_tuple = tuple()


# Q-2 tuple with items

dc_heros = ('superman', 'batman', 'wonder woman', 'shazzam', 'black adam')
marvel_heros = ('captain america', 'iron man', 'thor', 'hulk', 'vision')

# Q-3 joining two tuples

super_heros = dc_heros + marvel_heros
print(super_heros)

# Q-4 length of tuple

print(len(super_heros))

# Q-5 modifying tuple

super_heros = list(super_heros)
print(type(super_heros))

super_heros.extend(['Thanos','Loki','Ultron'])

print(super_heros)

marvel_characters = tuple(super_heros)

print(marvel_characters)
print(type(marvel_characters))