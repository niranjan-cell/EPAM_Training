"""
import unittest

class A( unittest.TestCase ):

    x = 1

    def test_func(self):
        # a = 1
        print(a)

    def test_one(self):
        print("Hello")
        print(1/0 )

        d = {}
        print( d['a'] )

    def test_two( self ):
        print( A.x + "Hi" )
        
if( __name__ == "__main__" ):
    unittest.main()
"""

"""
class A:

    def input( self ): # self = ob1
        self.x = int( input( "x = " ) ) # ob1.x = ...
        self.y = int( input( "y = " ) ) # ob1.y = ...
        
    def add( self ): # self = ob1
        print( f"add, self = {self}" )
        print( f"add, self.x = {self.x}" )
        print( f"add, self.y = {self.y}" )
        return self.x + self.y # ob1.x + ob1.y

ob1 = A()
ob2 = A()

# print( ob1.add(2, 3 ) )
# or

ob1.input() # or A.input( ob1 )

ob2.input() # or A.input( ob2 )

print( f"ob1.x = { ob1.x }" )
print( f"ob1.y = { ob1.y }" )
print( f"ob2.x = { ob2.x }" )
print( f"ob2.y = { ob2.y }" )


print( ob1.add() ) # or A.add( ob1 ) 
"""


import pandas as pd

