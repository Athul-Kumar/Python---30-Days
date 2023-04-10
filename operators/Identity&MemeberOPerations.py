
"""
                MEMEBERSHIP OPERATORS

1.in-operator ==> check if a character/substring/element exists in a sequence or not
2.not in-operator ==> Evaluate to true if it does not finds a variable in specified sequence and false otherwise


"""
# Examples

name = "Athul Kumar M U"
letter = 'b'

if letter in name: print("letter is present")
else: print("not present")

num_list = [10,20,30,40,50,60,70]

num = [30,7,8,20,60]

for nums in num_list:

    if nums in num:
        print("numbers overlapping", nums)
    else:print("numbers not overlapping", nums)



#  not in

item = "orange"

fruits = ['apple', 'mango', 'grapes', 'melon', 'lemon']

for fruit in fruits:

    if item not in fruit: print("True , orange is not presented in fruit list")
    else: print("False , orange is presented in fruit list")


"""
                        IDENTITY OPERATORS                        
Used to compare the objects if both the objects are actually of the same
 data type and share the same memory location
 
 is-operator ==> Evalutes to true if both variables on either side of the operator points
 to the same object and false otherwise
 
 is-not operator ==> Evalutes true if both variables  are not the same object
"""
   


num_1 = 5
num_2 = num_1

if id(num_1) is id(num_2):
    print("True", id(num_1), id(num_2))
else:
    print("False", id(num_1), id(num_2))