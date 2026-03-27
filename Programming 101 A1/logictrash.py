'''if s.isaplpha()
elif s in letters
print("Good guess", get_word_progress(secret_word,letters_guessed ))
                print("------")
print(" Oops! That letter is not in my word:",get_word_progress(secret_word,letters_guessed ))
                print("------")
                
if guess_alpha.isalpha():
            
            letters_guessed.append(guess_alpha)
            guesses -= 1
            if guess_alpha in secret_word and :
                print("Good guess", get_word_progress(secret_word,letters_guessed ))
                print("------")
            else:
                print(" Oops! That letter is not in my word:",get_word_progress(secret_word,letters_guessed ))
                print("------")
        
        else:
            print("Enter an alphabet only")
            
            if guess_alpha in letters_guessed:
                print("The letter has already been guessed")
                
        if 
            print("Congratulations, you won!")
            break
        else:
            print("you lost the match")
            print("The word to  be guessed was: ", secret_word)
            
         def hint(secret_word, available_letters):
            choose_from = ''
            available_letters = get_available_letters(letters_guessed)
            for letter in secret_word:
                if letter in available_letters:
                    choose_from = choose_from + letter
            new = random.randint(0, len(choose_from)-1)
            revealed_letter = choose_from[new]

right or wrong logic no code providence   '''
            
secret_word = 'asleep'            
copy = []
for i in range(len(secret_word)):
    if secret_word[i] not in secret_word[i+1:]:
        copy.append(secret_word[i])
    unique_letters =   ''.join(copy)  
print(len(unique_letters))
            
            
            