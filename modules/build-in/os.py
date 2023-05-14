
'''

                    Important Build-in Modules in python


1.OS Modules

    --> automatically perform many os tasks.
    --> os module provides functions for creating,
    --> changing current working directiory,
    -->  remove a directory,
    --> fetching its contents,
    --> changing and identifying current directory


        OS Functions

1.to get location of current working directiory = os.getcwd()

'''


#   OS MODULES

import os

# 1. current working directory

cwd = os.getcwd()

print("current working directory:", cwd)


# 2. changing current working directory

def current_path():
    print("current working directory before")
    print(os.getcwd())
    print()


current_path()

os.chdir('/')

current_path()

3.Creating Directory

directory = "modulePractice"

parent_dir = '/modules'

path = os.path.join( parent_dir, directory)

os.mkdir(path)


# removing a directory

dir = os.getcwd()

delete_dir = os.rmdir('modulePractice')
# print(delete_dir)