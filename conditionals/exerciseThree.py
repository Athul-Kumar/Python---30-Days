
person ={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


# Question-1

if 'skills' in person:
    print(f"The middle skill from skill key is : {person.get('skills')[2]}")


# method two

print(f"The middle skill from skill key is : {person['skills'][2]}") if 'skills' in person else print("no skill set")



#  Question -2

if 'skills' in person:
    print("True")
    if 'Python' in person['skills']:
        print(f"The person dict contains skills dict and in that dict {person.get('skills')[4]} is present")

else:
    print("python is not present")


# Question - 3

if person['skills'] == ['JavaScript', 'React']:
    print(f"He is a front end developer {person['skills']}")

elif person['skills'] == ['Node', 'Python', 'MongoDB']:
    print('He is a backend developer')

elif person['skills'] == ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']:
    print('He is a fullstack developer')

else:
    print(f"Unknown title, {person['skills']}")


#  Question-4

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")