#====================================
# Assignment 1, hangman.py
# Name: Natasha Shireen Williams
# Roll no: 291250392
# Section: A
# Time spent: 
#====================================

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    L = []
    found = False
    for i in secret_word:
        if i in letters_guessed :
            L.append(True)
        else:
            L.append(False)
    found = all(L)	#returns True if all items in the list is True
    return found
    
    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"

""


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    #secret_word = "apple"
    #letters_guessed = ["d","g","p","w"]
    s = []
    for i in secret_word:
        if i in letters_guessed:
            s.append(i)
        else:
            s.append("*")
            
    r = ''.join(s) #converts list s into string
    return r

    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   


def get_available_letters(letters_guessed):
    
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    
    s = []
    for i in string.ascii_lowercase:
        if i not in letters_guessed:	#letter that have not been guessed
            s.append(i)
    return ''.join(s)
        

    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    


def hint(secret_word, available_letters):
    ''' secret_word: string, the lowercase word the user is guessing
        available_letters:function, returns the letters that have not been guessed yet'''
    choose_from = ''
    #available_letters = get_available_letters(letters_guessed)
    for letter in secret_word:
        if letter in available_letters: #if letter in secret_word is available i.e it is not guessed yet concatenate it to choose_from
            choose_from =  choose_from + letter
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new] #stores a random letter from choose_from string
    return revealed_letter
        
    
def number_of_unique_letters_secret(secret_word):
    ''' secret_word: string, the lowercase word the user is guessing '''
    copy = []
    for i in range(len(secret_word)):
        if secret_word[i] not in secret_word[i+1:]:#checks if the letter does not repeat in the rest of the string
            copy.append(secret_word[i]) #appends the letter in  list  
    unique_letters =   ''.join(copy)  	# converts copy list into string
    return len(unique_letters)  
    
def hangman(secret_word, with_help):
    print("Welcome to Hangman")
    length_of_secret = len(secret_word)
    guesses = 10
    print(f"I am thinking of a {length_of_secret} letters word")
    print("-" * 14)
    letters_guessed =[]
    while guesses > 0 and not has_player_won(secret_word,letters_guessed):
        print(f"You have {guesses} guesses left.")
        print("Available letters: ",get_available_letters(letters_guessed))
        guess_alpha = input("Please guess a letter: ").lower()				
        if (with_help == True) and (guess_alpha == '!'):		#checks for  if the asked for help
            if guesses <= 3:
                print("You have less than three guesses. Try it yourself") #WARNING to the User
                
            else:
                hints = hint(secret_word,get_available_letters(letters_guessed)) #if hints are greater than or equal to 3
                letters_guessed.append(hints)
                print("Letter revealed:", hints)
                print("Good guess:", get_word_progress(secret_word,letters_guessed ))
                guesses -= 3
        #In all the conitions below the user loses no guesses
        elif not guess_alpha.isalpha(): #if not an alphabet
            print("Oops! That is not a valid letter. Please input a letter from the alphabet",get_word_progress(secret_word,letters_guessed ))
        elif guess_alpha in letters_guessed: #if the guessed letter has  already been guessed 
            print("The letter has already been guessed")
        elif guess_alpha in secret_word: # if guessed letter is correct i.e present in secret_word
            letters_guessed.append(guess_alpha)
            print("Good guess:", get_word_progress(secret_word,letters_guessed ))
            


        else: #The user inputs incorrect guesses which results in loss of guesses
            if guess_alpha not in letters_guessed and guess_alpha not in secret_word and guess_alpha not in 'aeiou':#consonants
                print("Oops! That letter is not in my word:",get_word_progress(secret_word,letters_guessed ))
                letters_guessed.append(guess_alpha)

                guesses -= 1
            elif guess_alpha in 'aeiou' and guess_alpha not in secret_word: #vowels
                print("Oops! That letter is not in my word:",get_word_progress(secret_word,letters_guessed ))
                letters_guessed.append(guess_alpha)
                guesses-= 2
                
        print("-"*14)
    if has_player_won(secret_word,letters_guessed): #Checks if the secret_word has been guessed or not
        print("Congratulations, you won!")
        total_score = (guesses + 4 *  number_of_unique_letters_secret(secret_word))+ (3 * len(secret_word))
        print('Your total score for this game is:',total_score)       
    else:
        print("Sorry, you ran out of guesses. You lost the match")
        print("The word to  be guessed was: ", secret_word)      

        
        
            
     
             
        
        
        
            
            
            
    
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)  #'wildcard'
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your assignment. However, please run test_a1_student.py
    # one more time before submitting to make sure all the tests pass.
    


