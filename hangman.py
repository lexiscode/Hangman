import random

print("##THE HANGMAN GAME##\n")

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

## GENERATE A RANDOM WORD ##
words = ['the', 'keywords', 'for', 'the', 'four', 'data', 'modifiers', 'are', 'signed', 'unsigned', 'short', 'and', 'long', 'you', 'also', 
         'going', 'learn', 'about', 'several', 'mathematical', 'functions', 'provided', 'by', 'language', 'such']
# Pick a word/string at random from the list above
rword_str = random.choice(words)

## GENERATE AS MANY BLANK-DASHES AS LETTERS IN THE WORD
# Convert the word/string to a list
space_join = ' '.join(rword_str)
rword_list = space_join.split()
print(rword_list)
# Replace the list indexes with dashes, then convert back to a string format
for i in range(len(rword_list)):
    rword_list[i] = ' __ '
    #print(rword_list)
#print(rword_list)  #rword_list has been updated with dashes as values
str_rword_list = ''.join(rword_list) #back to string
print(f"Guess the letters: {str_rword_list}\n") 

##Numbers of 6 tries when word ain't in the letters
life_lines = 0

end_of_game = False
while end_of_game == False:
    ##ASK THE USER TO GUESS A LETTER
    guessed_letter = input("Guess a letter: ")
    guessed_letter.lower()

    #CHECK IF THE GUESSED LETTER IS IN THE WORD
    for i in range(len(rword_str)):
        letter = rword_str[i]

        if letter == guessed_letter:
            rword_list[i] = letter
            #print(rword_list)
        #print(rword_list)
    # Change rword_list back to string
    str_rword_list = ''.join(rword_list) #back to string
    print(str_rword_list)

    #CHECK IF ALL THE BLANK-DASHES ARE FILLED OR NOT
    if '__' not in str_rword_list:
        end_of_game = True #Stops the while loop
        print("\nYOU WIN!!!")

    #WHEN GUESSED LETTER IS NOT PRESENT
    if guessed_letter not in rword_str:
        life_lines += 1
        if life_lines == 6:
            end_of_game = True #Stops the while loop
            print("YOU LOSE!")

    print(stages[life_lines])
