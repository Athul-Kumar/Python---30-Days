"""
                                MODULES

** module could be a file that containing a single variable, a function or a big code base

** a module can be included to an Application

** Modules have a specific functionality

** A module has a name specified by the filename without .py extension


1.creating a module ---> inside mymodule.py file

2.importing a module ---> mymodule is importing in test.py file
    * importing module   ---> import module
    * importing function from module ---> from module import function
    * importing functions from a
        module and renaming     ---> old function as new function

        (from module import old function as new function)


    * import every object from a module --> from module name import *

                        ' Python module search path using sys'


usecase --> when to import modules in different directiory their will be difference in
            order for proper import that will lead to error to avoid this using sys

example --> import sys
            sys.path.append("directory with base folder"
            import module(you want)


***************Importance of __name__ ****************

** Often, you want to write a script that can be executed directly or imported as a module.
    The __name__ variable allows you to do that.

** When you run the script directly, Python sets the __name__ variable to '__main__'.

    example --> check foo.py file line 19

                result = __main__


    print result --> before import
                    before function_a
                    before function_b
                    before __name__ guard
                    after __name__ guard



** However, if you import a file as a module,
    Python sets the module name to the __name__ variable.

    example --> foo is imported as a module

                result == foo


    print result --> before import
                        before function_a
                        before function_b
                        before __name__ guard
                        Function A
                        Function B 10.0
                        after __name__ guard


** Therefore, the __name__ variable allows you to check when the
    file is executed directly or imported as a module.

imp --> '__main__' --> script file
        __name__  --> module

        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# important Build-in Modules

"""

import foo