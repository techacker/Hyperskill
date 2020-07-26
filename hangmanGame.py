#! python3
# hangmanGame.py    -   A word guessing game against computer.

# 1. In the main menu, a player can choose to either play or exit the game;
# 2. If the user chooses to play, the computer picks a word from a list: this will be the riddle;
# 3. The computer asks the player to enter a letter that (s)he thinks is in the word;
# 4. If there's no such letter in the word and this letter hasn't been tried before, the computer counts it as a miss. A player can afford only up to 8 misses before the game is over;
# 5. If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
# 6. When the entire word is uncovered, it's a victory! The game calculates the final score and goes back to the main menu.


import random, re
print('H A N G M A N')

listofWords = ['python', 'java', 'kotlin', 'javascript']

# Choose randomly from the listofWords
chosenWord = random.choice(listofWords)
replacedWord = '-'*len(chosenWord)

attempt = 8
gameNotOver = True
typedLetter = []            # An empty list to capture unmatching letters

# Ask the user if they want to play the game.
playorNot = input('Type "play" to play the game, "exit" to quit: ')
if playorNot == 'play':
    gameNotOver = True
elif playorNot == 'exit':
    gameNotOver = False
else:
    input('Type "play" to play the game, "exit" to quit:')

# Check if the chosenWord letter matches the input from user.
while gameNotOver:
    print()
    print(replacedWord)
    char = input('Input a letter: ')
    # Check if the char is more than one letter
    if len(char) > 1:
        print('You should input a single letter')
    # Check if the char has special characters or is in CAPS
    elif not char.isalpha() or char.isupper():
        print('It is not an ASCII lowercase letter')   
    else:
        # Check if the char is in chosenWord and has not been entered earlier
        if char in chosenWord and char not in replacedWord and char not in typedLetter:
            # Check if the letter appears multiple times
            for letter in re.finditer(char, chosenWord):
                replacedWord = replacedWord[:letter.start()] + char + replacedWord[letter.start()+1:]
                if replacedWord == chosenWord:
                    print('You guessed the word '+ replacedWord + '!\nYou survived!')
                    gameNotOver = False
        # Check if the char is already entered and is in the replacedWord
        elif char in replacedWord and char not in typedLetter:
            print('You already typed this letter')
        # Check if the char is in the unmatching characteres list
        elif char in typedLetter:
            print('You already typed this letter')
        else:
            print('No such letter in the word ')
            # Add this unmatching character to the typedLetter list
            typedLetter.append(char)
            attempt = attempt - 1
            if attempt == 0:
                print('You are hanged!')
                gameNotOver = False
