'''s = len(secret_word) * "*"
    for i in letters_guessed:
        if i in secret_letter:
            s = i + s[1:len(s)]'''

'''secret_word = "apple"
letters_guessed = ["d","g","p","w"]
s = []
for i in secret_word:
    if i in letters_guessed:
        s.append(i)
    else:
        s.append("*")
        
r = ''.join(s)
print(r)'''
import string
'''letters_guessed = ["a","b","c"]
s = []
for i in string.ascii_lowercase:
    if i not in letters_guessed:
        s.append(i)
    
        
print(''.join(s))'''



'''def get_word_progress(secret_word, letters_guessed):
    #secret_word = "apple"
    #letters_guessed = ["d","g","p","w"]
    s = []
    for i in secret_word:
        if i in letters_guessed:
            s.append(i)
        else:
            s.append("*")
            
    r = ''.join(s)
    return r
print(get_word_progress("apple",["d","a","p","w"] ))'''

def has_player_won(secret_word, letters_guessed):
    L = []
    has_won = False
    for i in letters_guessed:
        if i in secret_word:
            L.append(True)
        else:
            L.append(False)
    has_won = all(L)
    return has_won



print(has_player_won('bass', ['a','s','b','e']))