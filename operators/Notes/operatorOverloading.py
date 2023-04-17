
"""
                            OPERATOR OVERLOADING

same built-in operator or function shows different behavior for objects of different classes,
this is called Operator Overloading.
"""

"""
                            How Does the Operator Overloading Actually work?
                            
                            
   Whenever you change the behavior of the existing operator through operator overloading, 
   you have to redefine the special function that is invoked automatically when the operator is used with the objects. 
   
   
            
        class A:
            def __init__(self, a):
                self.a = a
         
            # adding two objects
            def __add__(self, o):
                return self.a + o.a
        ob1 = A(1)
        ob2 = A(2)
        ob3 = A("Geeks")
        ob4 = A("For")
         
        print(ob1 + ob2)
        print(ob3 + ob4)
        # Actual working when Binary Operator is used.
        print(A.__add__(ob1 , ob2))
        print(A.__add__(ob3,ob4))
        #And can also be Understand as :
        print(ob1.__add__(ob2))
        print(ob3.__add__(ob4))             

"""

"""
                        BINARY OPERATORS
                        
                        Operator	Magic Method
                        +	__add__(self, other)
                        –	__sub__(self, other)
                        *	__mul__(self, other)
                        /	__truediv__(self, other)
                        //	__floordiv__(self, other)
                        %	__mod__(self, other)
                        **	__pow__(self, other)
                        >>	__rshift__(self, other)
                        <<	__lshift__(self, other)
                        &	__and__(self, other)
                        |	__or__(self, other)
                        ^	__xor__(self, other)
"""

"""
                        COMPARISON OPERATOR
                        
                        Operator	Magic Method
                        <	__lt__(self, other)
                        >	__gt__(self, other)
                        <=	__le__(self, other)
                        >=	__ge__(self, other)
                        ==	__eq__(self, other)
                        !=	__ne__(self,

"""


"""
                        ASSIGNMENT OPERATORS
                        
                        Operator	Magic Method
                        -=	__isub__(self, other)
                        +=	__iadd__(self, other)
                        *=	__imul__(self, other)
                        /=	__idiv__(self, other)
                        //=	__ifloordiv__(self, other)
                        %=	__imod__(self, other)
                        **=	__ipow__(self, other)
                        >>=	__irshift__(self, other)
                        <<=	__ilshift__(self, other)
                        &=	__iand__(self, other)
                        |=	__ior__(self, other)
                        ^=	__ixor__(self, other)

"""

"""
                        UNARY OPERATORS
                        
                        Operator	Magic Method
                        –	__neg__(self)
                        +	__pos__(self)
                        ~	__invert__(self)

"""