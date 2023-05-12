
# importing a module
import mymodule
print(mymodule.generate_full_name("athul", "kumar"))



#importing function from a module
from mymodule import generate_full_name

print(generate_full_name("Money", "Luffy"))
#
# importing functions from a module and renaming

from mymodule import generate_full_name as complete_name, sum_of_num as total

print(complete_name('Naruto', 'uzumaki'))
print(total(10,20))

"""
old module name as new module name
"""