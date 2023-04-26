"""

        Dictionary Exercises
"""

# 1.Create an empty dictionary called dog

# method-1

dog = {}
print(type(dog))
# method-2

dogs = dict()
print(type(dogs))

# 2.Add name, color, breed, legs, age to the dog dictionary

dog['name'] = "kisse"
dog.update({'color':'black'})
dog['Breed'] = "German"
dog.update({"legs": 4})
dog['age'] = 4

print(dog)

# 3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dict = {'first_name':'optimus',
                'last_name': 'prime',
                'gender': 'male',
                'age': 1000,
                'marital_status': 'Unmarried',
                'skills': ['autobots','last prime', 'leader', 'matrix holder', 'warrior'],
                'country': 'cybertron',
                'city':'Autobots city',
                'address':{
                    'city':'autobot city',
                    'country': 'cybertron',
                    'zip code': '999999'

                }
              }

print(student_dict.keys())

# 4.Get the length of the student dictionary

print(len(student_dict))

# 5.Get the value of skills and check the data type, it should be a list

student_skill = student_dict.get('skills')
print(type(student_skill))

# 6.Modify the skills values by adding one or two skills

student_dict['skills'] = ['Brave', 'died once']
print(student_dict)

# 7.Get the dictionary keys as a list

print(student_dict.keys())

# 8.Get the dictionary values as a list

print(student_dict.values())

# 9.Change the dictionary to a list of tuples using items() method

print(student_dict.items())

# 10.Delete one of the items in the dictionary
del student_dict['address']
print(student_dict)

# 11.Delete one of the items in the dictionary
del student_dict
# print(student_dict)