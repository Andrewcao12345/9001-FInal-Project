# install dict random word , pip install random-word

# initialising variables 
from random_word import RandomWords
r = RandomWords()
word = r.get_random_word() # initialize the word for the game 
progress = '_' * len(word) 
guesses = []

# starting text for the game , telling how long the word to guess is 

print(f'Welcome to game of hangman! I hope you know how to play cuz im not gonna explain')
print(f'The word has {len(word)} letters.')
print('The word is:', progress)

while True: # loop for correct errors input 
    try: 
        errors = int(input('How many errors are allowed? '))
        if errors < 0: 
            print('You must be allowed at least an error! Who do you think you are Einstein?')
        else: 
            break
    except ValueError: # if errors occur e.g a str is input and cant be int() it will print ... 
        print('Put in a number dingus')

while errors > 0: # loop for while not dead / errors > 0
    flag = False 
    tempprogress = ''
    guess = input('Guess a letter: ').lower()
    if len(guess) != 1 or guess.isalpha() == False: # .isalpha is checking it is in alphabet 
        print('Do you know what 1 letter is? Enter a single letter!!!!!!!') 
        continue
    if guess in guesses: # cant repeat letter, guesses are stored in list gusses to stop duplicate guesses
        print('You have already tried that letter dumbo!')  
        continue
    guesses.append(guess)

    for i in range(len(word)):
        if word[i] == guess:
            flag = True
            tempprogress += word[i]
        elif progress[i] != '_': # tempprogress is emptied everytime (line 29) so this is to keep previous guesses
            tempprogress += progress[i]
        else:   
            tempprogress += '_'
    if flag == False: 
        errors -= 1
        print(f'Wrong guess! Only {errors} guesses left.')
        if errors == 0:
            print('You have failed, stickman was hung, the word was:', word)
      
    if flag == True: 
        if tempprogress == word:
            print('Congrats! You have completed hangman without stickman being hung!')
            progress = tempprogress
            print(progress) # the loop breaks and doesnt print so must be printed here 
            break
        else: 
            print('Good job, your nearly there!')
    progress = tempprogress
    print(progress)





