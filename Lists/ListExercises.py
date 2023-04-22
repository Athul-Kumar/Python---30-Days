
#  Q-1

my_list1 = []

my_list2 = list()

print(type(my_list1))
print(type(my_list2))

# Q-2

clubs = ['Man.United', 'Man.City', 'Arsenal', 'Liverpool', 'Chelsea']

#  Q-3
print(len(clubs))

# Q-4

# using indexing

first_item = clubs[0]
middle_item = clubs[2]
last_index = len(clubs)-1
last_item = clubs[last_index]
print(first_item)
print(middle_item)
print(last_item)

#  using slicing
requ_items = clubs[0:5:2]
print(requ_items)


# Q-5
mixed_data_types = ['zorro', 35, 1.82, 'unmarried', {'address':'One piece world'}]

#  Q-6

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Q-7

print(it_companies)

# Q-8

numb_of_companies = len(it_companies)
print(numb_of_companies)

# Q-9

first_company = it_companies[0]
middle_company = it_companies[3]
last_index = len(it_companies)-1
last_company = it_companies[last_index]
print(first_company)
print(middle_company)
print(last_company)

#  Q-10

it_companies[0] = 'Meta'
print(it_companies)

# Q-11

it_companies.append('spotify')
print(it_companies)

# Q-12

it_companies.insert(4, 'Cred')
print(it_companies)

#  Q-13

it_companies[2] = it_companies[2].upper()
print(it_companies)

# Q-14

# it_companies = "#;".join(it_companies)
# print(it_companies)
# print(type(it_companies))
# it_companies = it_companies.split(';')
# print(it_companies)
# print(type(it_companies))

# Q-15

print('Google' in it_companies)
print(it_companies)

# Q-16

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

it_companies = sorted(it_companies)
print(it_companies)

# Q-17
print(it_companies)
it_companies.reverse()
print(it_companies)

# Q-18

print(it_companies)
print(it_companies[0:3])
print(it_companies[:3])


# Q-19

print(it_companies[-3:])
last_index = len(it_companies)-1
print(it_companies[last_index])
print(it_companies[6: last_index+1])

# Q-20

print(it_companies)
print(it_companies[3:6])
# Q-21
it_companies.pop(0)
print(it_companies)

# Q-22
it_companies.pop(4)
print(it_companies)

# Q-23
last_index = len(it_companies)-1
it_companies.pop(last_index)
print(it_companies)


# Q-24

it_companies.clear()
print(it_companies)

# Q-25

del it_companies
# print(it_companies)

# Q-26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

new_list = front_end + back_end
print(new_list)

# Q-27

full_stack = new_list.copy()
print(full_stack)




