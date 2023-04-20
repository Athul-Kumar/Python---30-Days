
"""
Lists --> is a collection which is ordered and changeable(modifiable, mutable).Allows duplicate members.
        A list can be empty or it may have different data type items

"""

"""
                    How to create a list
                    
method-1 --> using list build-in function

lst = list() #this is an empty list

method-2 --> using square brackets[]

lst = []  #this is an empty list

                    How to find methods associated with list using terminal
                    
new_list = [item_1,item_2,item_3]

1.dir(new_list)

                To know more about the method
                
help(new_list.methodName)

"""

# lists with initial values.We use len() to find the length of  a list

fruits = ['banana', 'orange', 'mango', 'lemon']
veggies = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
diary_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Postgres']
countries = ['India', 'Nepal', 'Bhutan', 'China', 'Korea']

# print lists and its length

print('fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', veggies)
print('Number of vegetables: ',len(veggies))
print('Diary products: ',diary_products)
print('Number of diary products: ', len(diary_products))
print('Web technologies: ', web_techs)
print('Number of Web technologies: ', len(web_techs))
print('Countries: ',countries)
print('Number of countries: ', len(countries))


"""
Also Lists can have items of different data types

"""
lst = ['Athul', 25, {'gender': 'Male'}, 60.50]
print(type(lst))
print(type(lst[2]))