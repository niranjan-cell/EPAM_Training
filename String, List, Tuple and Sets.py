"""
word = "ABC"
#index: 012
      # -3-2 -1

print( word )
print( word[0] )
print( word[1] )
print( word[2] )
print()
print( word[-1] )
print( word[-2] )
print( word[-3] )
"""


word = "Hello, How are you ?"
#index: 0123456789.....
# 

"""
print( word[3] )
print( word[4] )
print( word[5] )
print( word[6] )
print( word[7] )
print( word[8] )
"""

# Slicing ->
    # string_Data[ start_index = 0 : end_index = last_index : incr/decr = 1 ]

# print( word )
# print( word[ start = 0 : end = last_index : incr/decr = 1 ] )
# print( word[ : : ] )

"""
>>> word[ 5 : : ]
', How are you ?'
>>> word[ 4 : : ]
'o, How are you ?'
>>> 
>>> 
>>> word[ 4 : 16 : ]
'o, How are y'
>>> 
>>> word[ 2 : 8 :  ]
'llo, H'
>>> word[ 2 : 9 :  ]
'llo, Ho'
>>> word[ 2 : 10 :  ]
'llo, How'
>>> 
>>> word[ : :  ]
'Hello, How are you ?'
>>> word[ : : 1 ]
'Hello, How are you ?'
>>> word[ : : 2 ]
'Hlo o r o '
>>> 
>>> word[ : : 3 ]
'Hl wry '
>>> word[ : : 4 ]
'Hooro'
>>> 
>>> word[ : : ]
'Hello, How are you ?'
>>> word[ 2 : : ]
'llo, How are you ?'
>>> 
>>> len( word )
20
>>> word[19]
'?'
>>> 
\
>>> 
>>> word[ 2 : : ]
'llo, How are you ?'
>>> word[ 2 : 19 : ]
'llo, How are you '
>>> word[ 2 : 20 : ]
'llo, How are you ?'

>>> 
>>> 
>>> word[ 5: 2: -1 ]
',ol'
>>> 
>>> word[ 9: 2: -1 ]
'woH ,ol'
>>> word[ : : -1 ]
'? uoy era woH ,olleH'
"""


## String Inbuilt Fucntions

"""
#1) len()
word = "Hello, How are you ? My name is Gautam"
#index: 0123456789.........19
# len : 123456789..........20

print( len( word ) )
# last_index = len(word) - 1

#2) Capitalize()
word = "hello, How aRe you ?"

print( word.capitalize() )


#3) count()
word = "Hello, How are you ? My name is Gautam How"

print( word )
print( word.count( 'a' ) )
print( word.count( 'z' ) )
print( word.count( 'How' ) )


#4) endsWith()
word = "Hello, How are you ? My name is Gautam How"

print( word )
print( word.endswith( "How" ) )
print( word.endswith( " How" ) )
print( word.endswith( "w" ) )
print( word.endswith( " How " ) )


#5) startsWith()

word = "Hello, How are you ? My name is Gautam How"

print( word )
print( word.startswith( "Hello" ) )
print( word.startswith( " Hello" ) )
print( word.startswith( "Hello, " ) )
print( word.startswith( "H" ) )
print( word.startswith( "Hello " ) )


#6) find()

word = "Hello, How are you ? My name is Gautam How"
#index: 0123456789........

print( "find"
       , word.find( "How" )
       )

print( "find"
       , word.find( "How", 0, len(word) )
       )

print( "find"
       , word.find( "How", 0, 5 )
       )

print( "find"
       , word.find( "How", 8 )
       )

# 7) index()

print( "index"
       , word.index( "How", 0, len(word) )
       )

print( "index"
       , word.index( "How", 8 )
       )

print( "index"
       , word.index( "How", 0, 5 )
       )

# String -> Im-mutable datatype
 # -> Does not allow change by index
 
word = "Hello"

print( word )
print( word[0] )

word[0] = 'Z'

print( word )
print( word[0] )


# 8) replace
word = "Hello, How are you ? My name is Gautam How"

print( word )
# word[ 7:10 ] = "now" -> Error

word = word.replace( "How", "now")

print( word )

# 9) rstrip() -> Removes the space from the right side
word = "        Hello, How are you ?             "

print( "word = ", word )
print( "rstrip", word.rstrip() )
print()


# 10) lstrip() -> Removes the space from the left side
word = "         Hello, How are you ?             "

print( "word = ", word )
print( "lstrip", word.lstrip() )
print()


# 11) strip() -> Removes the space from left and right side
word = "         Hello, How are you ?             "

print( "word = ", word )
print( "strip", word.strip() )
print()


# 12) lower and upper()
word = "Hello, How are you %%$%is 234324 Gautam How"
print( "word = ", word )
print( "word.lower() = ", word.lower() )
print( "word.upper() = ", word.upper() )
print( "word.swapcase() = ", word.swapcase() )

# 13) title()
word = "Hello, How are you %%$%is 234324 gautam How"
print( "word = ", word )
print( "word.title() = ", word.title() )
"""


# Is functions
"""
# 1) isalpha()
print( "abcd .isalpha() = ", "abcd ".isalpha() )
print( "abcd.isalpha() = ", "abcd".isalpha() )
print( "ab12cd.isalpha() = ", "ab12cd".isalpha() )
print( "abCDe.isalpha() = ", "abCDe".isalpha() )
print( "ABCD.isalpha() = ", "ABCD".isalpha() )

# 2) isdigit()
print( "123.isdigit() = ", "123".isdigit() )
print( "123.5 -> isdigit() = ", "123.5".isdigit() )
print( "123abcd.isdigit() = ", "123abcd".isdigit() )
print( "abcd123.isdigit() = ", "abcd123".isdigit() )
print( "123abcd@$#@#.isdigit() = ", "123abcd@$#@#".isdigit() )
print( "abcd@$#@#.isdigit() = ", "abcd@$#@#".isdigit() )
print()

# 3) isdecimal()
print( "123.isdecimal() = ", "123".isdecimal() )
print( "123.5 -> isdecimal() = ", "123.5".isdecimal() )
print( "123abcd.isdecimal() = ", "123abcd".isdecimal() )
print( "abcd123.isdecimal() = ", "abcd123".isdecimal() )
print( "123abcd@$#@#.isdecimal() = ", "123abcd@$#@#".isdecimal() )
print( "abcd@$#@#.isdecimal() = ", "abcd@$#@#".isdecimal() )


# 4) istitle()

word = "Hello, How are you %%$%is 234324 gautam How"
word_title = word.title()

print( "word = ", word )
print( "word_title = ", word_title )
print( "word.istitle() = ", word.istitle() )
print( "word_title.istitle() = ", word_title.istitle() )


# 5) isspace()

print( " ".isspace() )
print( "1".isspace() )
print( "A".isspace() )
print( "A 1".isspace() )
print( "            ".isspace() )

# 6) isalnum()

print( "".isalnum() )
print( "123".isalnum() )
print( "abc".isalnum() )
print( "ABC".isalnum() )
print( "ABCabc".isalnum() )
print( "ABCabc123".isalnum() )
print( "ABCabc 123".isalnum() )

# 7) islower()

print( "ABC12123 GD".islower() )
print( "abc12123 GD".islower() )
print( "abc12123 gd".islower() )

# 8) isupper()

print( "ABC12123 GD".isupper() )
print( "abc12123 GD".isupper() )
print( "abc12123 gd".isupper() )
"""

"""
# Assignment : W3resource Strings Exercise :-  https://www.w3resource.com/python-exercises/string/

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$'
#    , except the first char itself. Go to the editor

# Sample String : 'restart'
# Expected Result : 'resta$t'

# Ex :- anamika -> an$mik$

word = "anamika"

print( word )
word = word[0] + word[1: : ].replace( word[0], "$" )
print( word )
"""


a = 5
b = 2.6
c = True
d = "HELLO"

# Expected Output : 52.6 True*Hello

"""
# f - method = { non_str area } str_area
print( "ab c*d" )
print( f"ab c*d" )
print( f"{a}b c*d" )
print( f"{a}{b} c*d" )
print( f"{a}{b} {c}*d" )
print( f"{a}{b} {c}*{d}" )
print( "{a}{b} {c}*{d}" )
print()
print( f"{a*5}{b} {c}*{d}" )
print()
print( f"a = {a} and b = {b} and a+b = { a+b }" )
print( f"a = {a} and b = {b} and a*b = { a*b }" )
"""

#####################LIST#############

# Brackets -> [] -> List, () -> Tuple, {} -> Set, Dictionary

# Existing
"""
a = 1
b = 5
c = 90
d = True
e = "SDsasa"
f = 5.6767
"""

"""
# Advance
x =    [ 1, 5, 90, True, "SDsasa", 5.6767 ]
#index   0  1  2   3      4        5
#len     1  2  3   4      5        6

print( f"x = { x }" )
print( f"type( x ) = { type( x )}" )
print( f"len(x) = { len(x) }" )
print( f"last_index = { len(x) - 1 }" )
print( f"x[ len(x) - 1 ] = { x[ len(x) - 1 ] }" )
"""

# List Inbuilt Functions

#######Add the data in the list#######
# 1) append()
"""
x = []

print( f"x = { x }" )
x.append( 5 )

print( f"x = { x }" )
x.append( 5.6 )

print( f"x = { x }" )
x.append( "Hello" )

print( f"x = { x }" )
x.append( False )

print( f"x = { x }" )
"""

# 2) insert()
"""
x = [5, 5.6, 'Hello', False]

print( f"x = { x }" )

x.insert( 2, True)
print( f"x = { x }" )

x.insert( 5, "Hi1")
print( f"x = { x }" )

x.insert( 100, "Hi2")
print( f"x = { x }" )


x.insert( -2, "Hi3")
print( f"x = { x }" )

x.insert( -200, "Hi4")
print( f"x = { x }" )
"""

#######Delete the data in the list#######
# 1) del -> delete by index or whole variable
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']

print( f"x = { x }" )

del x[2]
print( f"x = { x }" )

del x[4]
print( f"x = { x }" )

del x[6]
print( f"x = { x }" )

# del x[10] -> Error, IndexError: list assignment index out of range
# del x
# print( f"x = { x }" ) # -> Error, NameError: name 'x' is not defined
"""

#2) pop() -> delete by index
# a) without index :- list_name.pop()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']

print( f"x = { x }" )

print( x.pop() )
print( f"x = { x }" )

print( x.pop() )
print( f"x = { x }" )

print( x.pop() )
print( f"x = { x }" )
"""

# b) without index :- list_name.pop()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']

print( f"x = { x }" )

print( x.pop(2) )
print( f"x = { x }" )

print( x.pop(4) )
print( f"x = { x }" )

print( x.pop(9) )   # Error, IndexError: pop index out of range
print( f"x = { x }" )
"""


# 3) remove -> delete by value
"""
y = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', True, 5, True]

print( f"y = { y }" )

y.remove( True )
print( f"y = { y }" )

y.remove( True )
print( f"y = { y }" )

y.remove( True )
print( f"y = { y }" )

# y.remove( True )        # -> Error, ValueError: list.remove(x): x not in list
print( f"y = { y }" )
"""


# Update the elements of list
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']

print( f"x = { x }" ) # ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']
x[2] = 2.33
print( f"x = { x }" ) # ['Hi4', 5, 2.33, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']
"""

# Copy()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi3', 'Hi1', 'Hi2']

print( f"x = { x }\n" )

t1 = x.copy()
t2 = x

x[2] = 2.33

print( f"x = { x }" )
print( f"t1 = { t1 }" )
print( f"t2 = { t2 }\n" )

t2[4] = 100

print( f"x = { x }" )
print( f"t1 = { t1 }" )
print( f"t2 = { t2 }\n" )
"""

# count()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi', 'Hi', 'Hi']

print( f"x = { x }\n" )
print( f"x.count( 5 ) = { x.count( 5 ) }" )
print( f"x.count( 'Hi' ) = { x.count( 'Hi' ) }" )
print( f"x.count( 100 ) = { x.count( 100 ) }" )
"""

# extend()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi', 'Hi', 'Hi']
y = [ 1, 2, 3 ]

print( f"x = { x }" )
print( f"y = { y }\n" )

# print( x + y )
x.extend( y )       # x = x + y

print( f"x = { x }" )
print( f"y = { y }\n" )
"""

# reverse()
"""
x = ['Hi4', 5, 5.6, True, 'Hello', False, 'Hi', 'Hi', 'Hi']

print( f"x = { x }" )

# x.reverse() # Way 1
x = x[ : : -1 ] # Way 2

print( f"x = { x }" )
"""

# sort()
"""
x = [ 6, 5, 5.6, 324, 42323456, 4423423, 2343]

print( f"x = { x }" )

x.sort( reverse = False )
print( f"x = { x }" )

# x = x[ : : -1 ]
# print( f"x = { x }" )
"""

# split() and join()
"""
word = "Hello, How are you ?"

print( f"word = { word }" )

word_list = word.split( "o" )

print( f"word = { word }" )
print( f"word_list = { word_list }" ) # ['Hell', ', H', 'w are y', 'u ?']


print( "$".join( word_list ) )
"""



# Assignment : W3resource Strings Exercise :-  https://www.w3resource.com/python-exercises/list/

# Tuples -> ()
"""
t = ( 5, 6, 7, 100, 8 )
# ind 0  1  2  3

print( f"t = {t} and type(t) = { type(t) }" )

# t[2] = 1  # TypeError: 'tuple' object does not support item assignment

# That's why Tuple is Im-mutable

# Insertion -> x, Not Possible
# Deletion -> x, Not Possible
# update by index -> x, Not Possible

# count
print( f"t.count( 5 ) = { t.count( 5 ) }" )
print( f"t.count( 100 ) = { t.count( 100 ) }" )
print()

# index
print( f"t.index( 5 ) = { t.index( 5 ) }" )
print( f"t.index( 100 ) = { t.index( 100 ) }" )


#Concatination
t1 = ( 1, 2, 3 )
t2 = ( 4, 5, 6 )

print( t1+t2 )
"""



# Set -> {} -> It does not allows the duplicate but there is no
# concept of indexing
"""

s1 = { 1, 7, 9, "True", "False", "ABCD", "SSA", "ABCD" }
s2 = { 11, 7, 9, "True", "Fe", "ABCD", "S", "BCD" }

print( f"s1 = {s1}" )
print( f"s2 = {s2}\n" )
print()

print( f"s1.difference( s2 ) = { s1.difference( s2 ) }" ) # s1 - s2 )
print( f"s1 = {s1}" )
print( f"s2 = {s2}\n" )

print( f"s1.intersection( s2 ) = { s1.intersection( s2 ) }" ) # s1 - s2 )
print( f"s1 = {s1}" )
print( f"s2 = {s2}\n" )

print( f"s1.union( s2 ) = { s1.union( s2 ) }" ) # s1 - s2 )
print( f"s1 = {s1}" )
print( f"s2 = {s2}\n" )
"""
