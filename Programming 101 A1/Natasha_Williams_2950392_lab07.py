#WalkThrough 1
def greet ( name ) :
    """ Takes a name and returns a greeting message """
    message = "Hello, " + name + "!"
    return message
# Test the function
result = greet ("Alice ")
print ( result )
result = greet ("Bob")
print ( result )

#WalkThrough 2
def calculate_area ( length , width ) :
    """ Calculate area of a rectangle
    Parameters :
    length : length of rectangle ( number )
    width : width of rectangle ( number )
    Returns :
    area of rectangle ( number )
    """
    return length * width
result = calculate_area ( 4 , 3 )
print ( result )

#WalkThrough 3

def make_counter ( start ) :
    """ Creates a counter that starts at ’start’"""
    count = start
    def increment () :
        """ Increment and return the count """
        nonlocal count # This means : use the ’count ’ from parent function
        count = count + 1
        return count
    return increment

# Create a counter starting at 0
counter1 = make_counter (0)

# Create a counter starting at 100
counter2 = make_counter (100)
print (" Counter 1:")
print ( counter1 () ) # 1
print ( counter1 () ) # 2
print ( counter1 () ) # 3
print ("\n Counter 2:")
print ( counter2 () ) # 101
print ( counter2 () ) # 102
print ("\n Counter 1 again :")
print ( counter1 () ) # 4 - it remembers !

#WalkThrough 4
def make_adder ( n ) :
    """ Creates a function that adds n to its input """
    def adder ( x ) :
        """ Add n to x"""
        return n + x
    return adder
# Create custom adders
add5 = make_adder (5)
add10 = make_adder (10)
add100 = make_adder (100)
print(make_adder(20)(7))
print(make_adder(2)(7))
print (" add5 (3) =", add5 (3) ) # 8
print (" add10 (3) =", add10 (3) ) # 13
print (" add100 (3) =", add100 (3) ) # 103

#WalkThrough 5
def make_math_function ( multiplier , adder ) :
        """ Creates a function that multiplies by ’multiplier ’
        then adds ’adder ’"""
        def calculate ( x ) :
            """ Multiply x by multiplier , then add adder """
            result = x * multiplier + adder
            return result
        return calculate
#Double and add 5: f(x) = 2x + 5
double_plus_5 = make_math_function (2 , 5)
# Triple and add 10: f(x) = 3x + 10
triple_plus_10 = make_math_function (3 , 10)
print ( double_plus_5 (3) ) # 2*3 + 5 = 11
print ( triple_plus_10 (3) ) # 3*3 + 10 = 19

#WalkThrough 6
# Lists use square brackets []
numbers = [10 , 20 , 30 , 40 , 50]
print (" Numbers :", numbers )
print (" Type :", type ( numbers ) )

print ("\n Accessing elements :")
print (" First element ( index 0):", numbers [0])
print (" Second element ( index 1):", numbers [1])
print (" Last element ( index -1):", numbers [ -1])
print (" Second to last ( index -2):", numbers [ -2])

print("\n List length :", len( numbers ) )
print ("\n Slicing :")
print (" First 3 elements [0:3]: ", numbers [0:3])
print (" Elements 1 -3 [1:4]: ", numbers [1:4])
print (" Last 2 elements [ -2:]:", numbers [ -2:])
print (" Every other element [::2]: ", numbers [::2])

#WalkThrough 7
#List are Mutable
shopping = [" milk ", " bread ", " eggs "]
print (" Original list :", shopping )
print (" List ID in memory :", id( shopping ))
#APPEND
print ("\ nAdding ’butter ’ to the end ...")
shopping.append (" butter ")
print (" After append :", shopping )
print (" List ID:", id( shopping ) , "← Same ID!")
#REMOVE
print("\n Removing ’bread ’...")
shopping . remove (" bread ")
print ("After remove :", shopping )
#INSERT
print ("\ nInserting ’cheese ’ at position 1... ")
shopping . insert (3 , " cheese ")
print(shopping[3])
print (" After insert :", shopping )
#SORTING ALPHABETICALLY
print ("\ nSorting alphabetically ...")
shopping . sort ()
print (" After sort :", shopping )
print (" List ID:", id( shopping ) , "← Still same ID")

#WalkThrough 8

sentence = " Python is an amazing language "
print (" Original sentence :", sentence )
words = sentence . split ('a')
print (" Split into words :", words )
s,c,a = words[0],words[1],words[2]
print(s,c,a)

colors = [" red", " green ", " blue "]
print ("\ nList of colors :", colors )
# The string before . join () is the separator
result = " ". join ( colors )
print (" Joined with spaces :", result )
result = ", ". join ( colors )
print (" Joined with commas :", result )
result = "-". join ( colors )
print (" Joined with dashes :", result )
print (" Number of words :", len( words ) )

