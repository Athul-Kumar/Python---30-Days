'''
                        SYS Module

---> allows you to work with system
---> sys module provides functions and variables used to manipulate different parts of the python
    runtime environment

---> Function sys.argv returns a list of command line arguments passed to a python script
        * item at index 0 in this list always the name of the script
        * at index 1 is the argument passed from the command line


usecase of sys

    1.You can access any command line arguments using sys.argv[1:]
    2.you can  see the path to the file
    3.version of your interpreter using sys.version
    4.Exit the running code with sys.exit

'''


import sys

# print('welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))


# result --> welcome Athul. Enjoy 30DaysOFPython challenge!


# to exit sys sys.exit()

# sys.exit()

# to show environment paths
path = sys.path
# print(path)

# to know version of python

v = sys.version

print(v)

window = sys.getwindowsversion()
print(window)