########################Comparision Operator -> > , < , == , != , >= , <=

"""
# INput :- numbers , Output :- Boolean

5>2 = True
2>5 = False

#######Changing the Comparision Operator/ Logical Operator -> and / or

# and( both )
True and True -> True
True and False -> False
False and True -> False
False and False -> False

#or ( anyone )
True or True -> True
True or False -> True
False or True -> True
False or False -> False

Input :- bool
Output :- bool

"""

"""
a = 2.5
b = 2
c = 3

print( f"a>b = { a>b } , a>c = { a>c } , ( a>b ) and ( a>c ) = { ( a>b ) and ( a>c ) }" )

print( f"a>b = { a>b } , a>c = { a>c } , ( a>b ) or ( a>c ) = { ( a>b ) or ( a>c ) }" )
"""

################Dictionary############

# Existing
# money = [ 25000 16000, 55000, 23000 ]


# Dictionary

#Creation
"""
money1 = {}

money2 = dict()

money3 = { "salary" : [ 16000, 23000 ]
          , "bonus" : [ 25000, 55000 ]
        }

print( f"money1 = { money1 } and type( money1 ) = { type( money1 ) }" )
print( f"money2 = { money2 } and type( money2 ) = { type( money2 ) }" )
print( f"money3 = { money3 } and type( money3 ) = { type( money3 ) }" )
"""


# Add data in dictionary
"""
d = {}

print( f"d = {d} and type(d) = { type(d) }\n" )

d["Name"] = [ "Ram", "Shyam", "Ram" ]
print( f"d = {d} and type(d) = { type(d) }\n" )

d["Empid"] = [ 1234, 5678, 1112 ]
print( f"d = {d} and type(d) = { type(d) }\n" )

d["Salary"] = [ 18000, 20000, 17000 ]
print( f"d = {d} and type(d) = { type(d) }\n" )

d["Name"] = "Ram1", "Shyam2"
print( f"d = {d} and type(d) = { type(d) }\n" )
"""

# get()
"""
d = {'Name': ['Ram1', 'Shyam2', 'Ram3']
     , 'Empid': [1234, 5678, 1112]
     , 'Salary': [18000, 20000, 17000]
     }

#print( d["Name1"] )
print()
print( d.get("Name1") )
"""

# pop()
"""
d = {'Name': ['Ram1', 'Shyam2', 'Ram3']
     , 'Empid': [1234, 5678, 1112]
     , 'Salary': [18000, 20000, 17000]
     }

print( f"d = {d}\n" )

print( d.pop("Name") )
print( f"d = {d}\n" )
"""

# del
"""
d = {'Name': ['Ram1', 'Shyam2', 'Ram3']
     , 'Empid': [1234, 5678, 1112]
     , 'Salary': [18000, 20000, 17000]
     }

print( f"d = {d}\n" )

del d["Name"]
print( f"d = {d}\n" )
"""


# popitem
"""
d = {'Name': ['Ram1', 'Shyam2', 'Ram3']
     , 'Empid': [1234, 5678, 1112]
     , 'Salary': [18000, 20000, 17000]
     }

print( f"d = {d}\n" )

print( f"d.popitem() 1 = { d.popitem() }" )
print( f"d = {d}\n" )

print( f"d.popitem() 2 = { d.popitem() }" )
print( f"d = {d}\n" )

print( f"d.popitem() 3 = { d.popitem() }" )
print( f"d = {d}\n" )

print( f"d.popitem() 4 = { d.popitem() }" )
print( f"d = {d}\n" )
"""

"""
d = {'Name': ['Ram1', 'Shyam2', 'Ram3']
     , 'Empid': [1234, 5678, 1112]
     , 'Salary': [18000, 20000, 17000]
     }

# keys()
print( f"Keys = { d.keys() }\n" )

# values()
print( f"values = { d.values() }\n" )

# items()
print( f"items = { d.items() }" )
"""

######## File Handling########
"""
# File_Options : *.txt, *.csv, *.xlsx , *.pdf, *.json , *.xml , etc

# *.txt
file_path = r"C:\Users\gauta\Desktop\F1.py"

# Access Method
# 1) 'r' -> read
# 2) 'w' -> Write
# 3) 'a' -> append
# 4) 'r+' -> read and Write

data = open( file_path, "r+" )

data.write( "Hello" )

print( data.read() )

data.close()
"""






