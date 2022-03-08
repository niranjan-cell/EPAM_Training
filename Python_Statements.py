##########Conditional Statements##########

# Statements
# a = 2, print( a )

# Conditional = Condition

# Conditional Statemnets = Any statements with Condtions

# Types of Conditional Statements,
# 1) if Condition
# Syntax :-
"""
if( condtion ): # Condtion -> True/ False
    Statement 1
    Statement 2
    .
    .
    Statement n
"""

"""
print( "Start" )

if( False ):
    a = 2
    print( a )

print( "End" )
"""

"""
a = 11
b = 2

print( "Start" )

if( a>b ): # a>b -> True/ False
    print( f"a = {a} and b = {b} and a>b = { a>b }" )

print( "End" )
"""

"""
a = 1
b = 2
c = 3

print( "Start" )

if( (a>b) and (a>c) ): # a>b -> True/ False
    print( f"a = {a}, b = {b}, c = {c} , a>b = { a>b } , a>c = { a>c }" )
    print( f"(a>b) and (a>c) = { (a>b) and (a>c) }" )

print( "End" )
"""

# 2) if-else Condition
# Syntax :-
"""
if( condtion ): # Condtion -> True/ False
    Statement 1
    Statement 2
    .
    .
    Statement n
else:
    Statement 1
    Statement 2
    .
    .
    Statement n
"""

# NOTE :- Else is always optional. Else meaning is otherwise

"""
a = 11
b = 2
c = 3

print( "Start" )

if( (a>b) and (a>c) ): # a>b -> True/ False
    print( f"IF : a = {a}, b = {b}, c = {c} , a is greater than b and c" )
else:
    print( f"ELSE : a = {a}, b = {b}, c = {c} , a is Smaller than b and c" )

print( "End" )
"""

# 3) elif ladder Condition
"""
if( condtion1 ): # Condtion -> True/ False
    Statement 1
    Statement 2
    .
    .
    Statement n

elif( condition2 ):
    Statement 1
    Statement 2
    .
    .
    Statement n

elif( condition3 ):
    Statement 1
    Statement 2
    .
    .
    Statement n

.
.
elif( condition n ):
    Statement 1
    Statement 2
    .
    .
    Statement n

else:         -> Optional
    Statement 1
    Statement 2
    .
    .
    Statement n
"""

"""
a = 15

print("Start" )

# Block 1
if( a > 0 ):
    print( f"{a} is Negative" )

# Block 2
if( a%3 == 0 ):
    print( f"{a} is divisible by 3" )

print( "End" )
"""

"""
a = 15

print("Start" )

# Block 1
if( a > 0 ):
    print( f"{a} is +ve" )

elif( a%3 == 0 ):
    print( f"{a} is divisible by 3" )

print( "End" )
"""


"""
a = 35

print("Start" )

# Block 1
if( a < 0 ):
    print( f"{a} is -ve" )

elif(a == 0 ):
    print( f"{a} is 0" )

elif( (a > 0) and ( a < 11 ) ):
    print( f"{a} is from 1 to 10" )

elif( (a > 10) and ( a < 21 ) ):
    print( f"{a} is from 11 to 20" )

elif( (a > 20) and ( a < 31 ) ):
    print( f"{a} is from 21 to 30" )

else:
    print( f"{a} is more than 30" )

print( "End" )
"""

# While Loop
"""
# C progarm

i = 1
while( i <= 10 )
{
    printf( i )
    i = i + 1
}

# Python progarm

i = 1
while( i <= 10 ):
    print( i )
    i = i + 1
"""

"""
print( "Start" )

i = 1
while( i <= 5 ):
    print( i )

    i = i + 1

print( "End" )
"""

# Find out which all numbers are perfectly divisble by 5 and 3
# between range 1 to 200
"""
print( "Start" )

count = 0
i = 1
while( i <= 200 ):

    if( (i%5 == 0) and (i%3 == 0) ):
        print( i )
        count = count + 1
    
    i = i + 1

print( f"End, count = {count}" )
"""


# For Loop
# 1) with Range
"""
# C progarm

for( i = 0 ; i<= 10 ; i++)
{
    print( i )
}
"""

# Python progarm

# for i in range( 1, 11, 1 ):
#     print( i )

# for i in range( 10, 0, -2 ):
#     print( i )


# 2) without Range
# for i in [1, 21, 16, 9, 10, True, "Hello"]:
#     print( i )



######Useful operators in Python#######

# Arithmetic Operators -> +, -, * , / , ** , //, %
# Comparision Operator -> > , < , == , != , >= , <=
# Membership Operator -> in, not in

"""
print( "H" in "Hello, How are you ?" ) # True
print( "He" in "Hello, How are you ?" ) # True
print( "Hel" in "Hello, How are you ?" ) # True
print( "Helo" in "Hello, How are you ?" ) # False
print( "Hello " in "Hello, How are you ?" ) # False
"""

"""
print( 2 in [ 2, 8, 90, 24, 5 ] ) # True
print( 20 in [ 2, 8, 90, 24, 5 ] ) # False
print( 5 in [ 2, 8, 90, 24, 5 ] ) # True
print( [2, 90] in [ 2, 8, 90, 24, 5 ] ) # False
print( [2, 8] in [ 2, 8, 90, 24, 5 ] ) # False
print( [ 2, 8] in [ 90, 24, 5, [2, 8] ] ) # True
"""

# 2( int ) in [ int, int, int, int, int ]
# [2, 90]( list ) in [ int, int, int, int, int ]

# [ 2, 8]( list ) in [ 90( int ), 24( int ), 5( int ), [2, 8](list) ]


##########List Comprehension##########

# l = [ 2, 5, 7, 8, 10 ]

# for i in l:
#     print( i )

# Syntax :- [ Child parent ]

# [ print( i ) for i in l  ]


# for i in l:
#     if( i%2 == 0):
#         print( i )

# op = [ i for i in l if( i%2 == 0) ]
# print( op )


# fruits = [ "apple", "orange", "Banana" ]
# op = [ i.upper() for i in fruits ]
# print( op )


"""
# Write a python Program which takes start and end from user and
# shows the cube of all the numbers

# O/p => 

start = 1
end = 10

# for i in range( start, end+1 ):
#     print( f"Number is : {i} and cube of the {i} is :{i**3}" )

op = [ f"Number is : {i} and cube of the {i} is :{i**3}" for i in range( start, end+1 ) ]

print( op )
"""


"""
18. Write a program in C to find the sum of the series [ 1-X^2/2!+X^4/4!- .........]. Go to the editor
Test Data :
Input the Value of x :2
Input the number of terms : 5
Expected Output :
the sum = -0.415873
Number of terms = 5
value of x = 2.000000
"""

"""
# n = 4 => 0, 2, 4, 6
# n = 5 => 0, 2, 4, 6, 8

x = 2

given_term = 5
curr_term = 1
power = 0
add = 0

while( curr_term != given_term+1 ):
    # print( f"curr_term = { curr_term } , given_term = { given_term }, power = { power }", end = ' ' )

    # Factorial Start
    fact = 1
    temp_power = power
    while( temp_power > 0 ):
        fact = fact * temp_power 

        temp_power = temp_power - 1
    # Factorial End


    # print( f"fact = { fact }" )
    if( curr_term%2 == 0 ):
        add = add - ( x ** power )/fact
    else:
        add = add + ( x ** power )/fact

    power = power + 2
    curr_term = curr_term + 1


print( f"Output = { add }" )
"""


##############Functions###########

"""
a = 2
b = 3
print(a+b)


a = 11
b = 12
print(a+b)

a = 21
b = 22
print(a+b)
"""

"""
# 3 times
for i in range(1, 4 ):
    a = int( input( "Enter 1st number = " ) )
    b = int( input( "Enter 2nd number = " ) )

    print( a + b )

print("Hello")
print(a*b)


# 3 times
for i in range(1, 4 ):
    a = int( input( "Enter 1st number = " ) )
    b = int( input( "Enter 2nd number = " ) )

    print( a + b )
"""

# Solution : Fucntions

#####How to create Functions in Python#######
# Functions = A Variable which can hold arguments and statements

# 'a' Variable holding value, a = 2

# 'f1' variable holding statement(s)

# Syntax :-
"""
def func_name():
    statement 1
    statement 2
    .
    .
    statement n
"""


"""
def f1():
    a = int( input( "Enter 1st number = " ) )
    b = int( input( "Enter 2nd number = " ) )

    print( a + b )

f1()
f1()
f1()
"""

######Passing the value from outside###
"""
def f1( a, b ): # a, b -> #FormalParameter/Argument
    
    print( f"a = {a} and b = {b} and a+b = { a+b }" )

f1( 2, 3 )      # Actual Parameter/Argument
f1( 12, 13 )      # Actual Parameter/Argument
f1( 22, 23 )      # Actual Parameter/Argument
"""
#########Taking the value Outside of Functions

"""
def f1( a, b ): # a, b -> #FormalParameter/Argument
    
    print( f"a = {a} and b = {b} and a+b = { a+b }" )

    return a+b, a-b, a*b, a/b

op1, op2, op3, op4 = f1( 2, 3 )

print( f"Outside , op1 = { op1 }" )
print( f"Outside , op1 = { op2 }" )
print( f"Outside , op1 = { op3 }" )
print( f"Outside , op1 = { op4 }" )
"""

"""
def message():
    print( "Hello World" )

message()
"""

"""
def message( name ):
    print( f"Hello {name}" )

message( "Gautam" )
"""

"""
def even_odd( num ):
    return num%2 == 0

print( even_odd(4) )
"""

"""
def isgreater( a, b ):
    if( a>b):
        return f"a = {a} , b = {b} and a is greater than b"
    else:
        return f"a = {a} , b = {b} and a is not greater than b"

print( isgreater( 3, 2 ) )


# Output :- a = 2 , b = 3 and a is not greater than b
"""



# *args -> arguments
"""
# Existing :- 
def f1( num1, num2, num3 ):
    return num1 + num2 + num3

op = f1( 2, 3, 4, 5 )

print( f"Sum = { op }" )
"""


# Soltuon :-
"""
def f1( *nums ):
    print( f"nums = { nums }" )

    add = 0
    for i in nums:
        add = add + i

    return add

op = f1( 2 )

print( f"Sum = { op }" )
"""

"""
def f1( a, b, *nums ):
    print( f"a = {a} , b = {b} , nums = { nums }" )

    add = a+b
    for i in nums:
        add = add + i

    return add

op = f1( 2, 3, 5, 9, 10 )

print( f"Sum = { op }" )
"""

"""
# Kwargs -> Keyword - arguments
def f1( a, b, *nums, **knums ):
    print( f"a = {a} and type(a) = { type(a) }" )
    print( f"b = {b} and type(b) = { type(b) }" )
    print( f"nums = { nums } and type(nums) = { type(nums) }")
    print( f"knums = { knums } and type(knums) = { type(knums) }" )

    add = a+b
    for i in nums:
        if( isinstance( i, int ) ):
            add = add + i

    for i in knums.values():
        if( isinstance( i, int ) ):
            add = add + i

    return add

op = f1( 2, 3, 5, 9, 10, c = 11, d = 12, e = 14, f = "Hi" )

print( f"Sum = { op }" )
"""

##########Exercises##########

#1) Write a Python function to find the Max of n numbers.
"""
def greater( *nums ):

    max_num = nums[0]
    for i in range( 1, len( nums ) ):
        if( max_num < nums[i] ):
            max_num = nums[i]
        
    return max_num

print( greater( -99999999992, -99999999993, -99999999997, -9999999999345, -99999999994565, -99999999994654, -999999999966, -9999999999645654 ) )
"""


# 2) Write a Python program to reverse a string.
"""
def reverse( str_data ):
    return str_data[ : : -1 ]

print( reverse( "1234abcd" ) )
"""

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
"""
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

"""
def count_char( str_data ):

    upper_count = 0
    lower_count = 0
    digit_count = 0
    
    for i in str_data:
        if( i.isupper() ):
            upper_count = upper_count + 1
            
        elif( i.islower() ):
            lower_count = lower_count + 1

        elif( i.isdigit() ):
            digit_count = digit_count + 1

    return upper_count, lower_count, digit_count

op = count_char( 'The quick Brow Fox 122345435313213' )

print( f"upper_count = { op[0] }" )
print( f"lower_count = { op[1] }" )
print( f"digit_count = { op[2] }" )
"""


"""
char      ord(  )           chr()
'a'       ord('a') -> 97    chr(97) -> 'a'
'b'       ord('a') -> 98
.
.
'z'       ord('a') -> 122

'A'       ord('A') -> 65
.
.
'Z'       ord('Z') -> 90

'0'       ord('1') -> 48
'1'       ord('1') -> 49
'2'       ord('2') -> 50
'3'       ord('3') -> 51
.
.
'9'       ord('3') -> 57
"""

"""
def count_char( str_data ):

    upper_count = 0
    lower_count = 0
    digit_count = 0
    
    for i in str_data:
        curr_ord = ord( i )

        if( (curr_ord>=65) and (curr_ord<=90) ):
            upper_count = upper_count + 1
            
        elif( (curr_ord>=97) and (curr_ord<=122) ):
            lower_count = lower_count + 1

        elif( (curr_ord>=48) and (curr_ord<=57) ):
            digit_count = digit_count + 1

    return upper_count, lower_count, digit_count

op = count_char( 'The quick Brow Fox 122345435313213' )

print( f"upper_count = { op[0] }" )
print( f"lower_count = { op[1] }" )
print( f"digit_count = { op[2] }" )
"""

# Map
"""
def cube( num ):
    print( f"num = {num}" )
    return num**3

def odd_even( num ):
    if( num%2 == 0 ):
        return num
    else:
        pass

l = [ 1, 2, 3, 4, 5, 6 ]


# op = map( cube, l )
op = map( odd_even, l )

print( list( op ) )
"""

"""
# filter
def odd_even( num ):
    print( f"num = { num }" )
    return num%2 == 0

l = [ 1, 2, 3, 4, 5, 6 ]

op = filter( odd_even, l )

print( list( op ) )
"""

# reduce
"""
from functools import reduce

def sum(n1, n2 ):
    print( f"n1 = {n1} , n2 = {n2}" )
    
    return n1+n2

l = [ 1, 2, 3, 4, 5, 6 ]

op = reduce( sum, l )

print( op )
"""

# lambda Functions
# Existing
"""
def cube( num ):
    return num**3

l = [ 1, 2, 3, 4, 5, 6 ]

op = map( cube, l )
print( list( op ) )
"""


# Using Lambda Function
# def cube( num ):
#     return num**3

# lambda num: num**3

# map + lambda
"""
l = [ 1, 2, 3, 4, 5, 6 ]

op = map( lambda num: num**3, l )
print( list( op ) )
"""

# reduce + lambda
"""
from functools import reduce

l = [ 1, 2, 3, 4, 5, 6 ]

op = reduce( lambda num1, num2 : num1+num2, l )
print( op )
"""

"""
def arithmetic( num1, num2 ):
    print( "Inside arithmetic\n" )
    
    def add( num1, num2 ):
        return f"Add = { num1+num2 }"

    def sub( num1, num2 ):
        return f"sub = { num1-num2 }"

    def mult( num1, num2 ):
        return f"mult = { num1*num2 }"

    def div( num1, num2 ):
        return f"div = { num1/num2 }"

    # add( a, b )
    # sub( a, b )
    # mult( a, b )
    # div( a, b )

    return add, sub, mult, div


a = 2
b = 3

op1, op2, op3, op4 = arithmetic(a, b )

# op1 = def add( num1, num2 ):
        # return f"Add = { num1+num2 }"

print( f"Outside")
print( op1( a, b) )
"""

######Scope######

a = 1

def f1():
    a = 2

    print( f"f1 Before , a = {a}" )

    def f2():
        global a
        a = 5

        print( f"f2 , a = {a}" )

    f2()
    print( f"f1 After , a = {a}" )
        
print( f"Outside Before, a = {a}" )
f1()
print( f"Outside After, a = {a}" )
