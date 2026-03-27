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

#D1 exercise

def make_greeting ( greeting_word ) :
    """ Creates a custom greeting function
    Example :
    say_hello = make_greeting (" Hello ")
    say_hello (" Alice ") returns "Hello , Alice !"
    """
    def greet ( name ) :
        return greeting_word + "," + name + "!"
    return greet

# Test your code
say_hello = make_greeting (" Hello ")
say_hi = make_greeting ("Hi")
say_hey = make_greeting ("Hey ")
print ( say_hello (" Alice ") ) # Should print : Hello , Alice !
print ( say_hi ("Bob") ) # Should print : Hi , Bob!
print ( say_hey (" Charlie ") ) # Should print : Hey , Charlie !

#D2 exercise

def double_all_elements ( numbers ) :
    """ Double every element in the list ( MUTATE the list )"""
    # BUG: This doesn ’t change the list !
    for i in range(len(numbers)):
        numbers[i] = numbers[i] *2
        
  
    # TODO : Fix this using indexing
    # Hint : for i in range (len( numbers )):
    # numbers [i] = ...
# Test
my_list = [1 , 2 , 3 , 4 , 5]
print (" Before :", my_list )
double_all_elements ( my_list )
print (" After :", my_list ) # Should be [2 , 4 , 6 , 8 , 10]


#D3 exercise

def count_words ( sentence ) :
    """ Count how many words are in a sentence """
    # TODO : Use split () to break sentence into words
    words = sentence.split()
    # TODO : Return the length of the words list
    return len(words)
# Test cases
print ( count_words (" Hello world ") ) # Should print : 2
print ( count_words (" Python is awesome ") ) # Should print : 3
print ( count_words ("I love programming ") ) # Should print : 3

#D4 exercise

def make_range_list ( start , end ) :
    """ Create a list of numbers from start to end ( inclusive )"""
    result = []
    for i in range(start, end+1):
        result.append(i)
    
    # TODO : Use a for loop with range () to add numbers to result
    # Remember : range (start , end +1) to include ’end ’
    return result
# Test
print ( make_range_list (1 , 5) ) # [1 , 2 , 3 , 4 , 5]
print ( make_range_list (10 , 15) ) # [10 , 11 , 12 , 13 , 14 , 15]


#E1 exercise

def calculate_average ( numbers ) :
    """ Calculate average of numbers in a list """
    # Step 1: Calculate sum
    sum =0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
        
    # Step 2: Divide by length
    result = sum/len(numbers)
    # Step 3: Return result
    return result
# Test cases
print ( calculate_average ([10 , 20 , 30]) ) # Should print : 20.0
print ( calculate_average ([5 , 15 , 25 , 35]) ) # Should print : 20.0
print ( calculate_average ([100]) ) # Should print : 100.0

#E2 exercise
def find_maximum ( numbers ) :
    """ Find the largest number without using max () """
    # Step 1: Start with first element
    current_max = numbers [0]
    # Step 2 -3: Loop and update if needed
    for i in range(len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_max = numbers[i]
    # Step 4: Return result
    return current_max
# Test
print ( find_maximum ([3 , 7 , 2 , 9 , 1]) ) # 9
print ( find_maximum ([15 , 8 , 23 , 4]) ) # 23

#E3 exercise

def remove_duplicates ( items ) :
    """ Remove duplicates , keep first occurrence """
    result = []
    found = True
    # Your code here
    for i in range(len(items)):
        if items[i] in result:
            found = True
        else:
            result.append(items[i])
            
    return result
# Test
print ( remove_duplicates ([1 , 2 , 2 , 3 , 1 , 4]) )

#E4 exercise
def reverse_words ( sentence ) :
    """ Reverse order of words in sentence """
    # Step 1: Split
    lis = sentence.split()
    
    # Step 2: Reverse
    rev = lis[-1::-1]
    
    # Step 3: Join
    new_list = ' '.join(rev)
    # Step 4: Return
    return new_list
# Test
print ( reverse_words (" Hello world ") ) # " world Hello "
print ( reverse_words (" Python is fun") ) # "fun is Python "

